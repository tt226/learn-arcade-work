"""
Background and ground layer are from:
https://kenney.nl/
https://itch.io/

Player resources are from:
https://pixelfrog-assets.itch.io/pixel-adventure-1

Music is from:
https://benjaminno.itch.io/sweet-sounds-sfx-pack?download
https://joshuuu.itch.io/short-loopable-background-music/download/

"""
import math
import os
import arcade

# constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "platformer"

# scale sprite from their original size
TILE_SCALING = 0.5
CHARACTER_SCALING = TILE_SCALING * 2
COIN_SCALING = TILE_SCALING * 2
SPRITE_PIXEL_SIZE = 32
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# movement speed of player
PLAYER_MOVEMENT_SPEED = 7
GRAVITY = 1.5
PLAYER_JUMP_SPEED = 30

# minimum margin between the character and the edge of the screen
LEFT_VIEWPORT_MARGIN = 200
RIGHT_VIEWPORT_MARGIN = 200
BOTTOM_VIEWPORT_MARGIN = 150
TOP_VIEWPORT_MARGIN = 100

PLAYER_START_X = 2
PLAYER_START_Y = 1
# facing right or left
RIGHT_FACING = 0
LEFT_FACING = 1

LAYER_NAME_MOVING_PLATFORMS = "Moving Platforms"
LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_COIN = "Coin"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_PLAYER = "Player"
LAYER_NAME_GHOST = "GHOST"


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True), ]


class Entity(arcade.Sprite):
    def __init__(self, name_folder, name_file):
        super().__init__()

        # Default to facing right
        self.facing_direction = RIGHT_FACING

        # Used for image sequences
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING

        main_path = f"player_resources/{name_folder}/{name_file}"
        self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")
        self.jump_texture_pair = load_texture_pair(f"{main_path}_jump.png")

        # walking animation
        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{main_path}_walk.png")
            self.walk_textures.append(texture)

        # initial texture
        self.texture = self.idle_texture_pair[0]

        # hit box
        self.set_hit_box(self.texture.hit_box_points)


class Ghost(Entity):
    def __init__(self, name_folder, name_file):
        # Setup parent class
        super().__init__(name_folder, name_file)


class PlayerCharacter(Entity):
    """player sprite"""

    def __init__(self):
        super().__init__("male_person", "malePerson")
        # track our state
        self.jumping = False

    def update_animation(self, delta_time: float = 1 / 60):
        if self.change_x < 0 and self.facing_direction == RIGHT_FACING:
            self.facing_direction = LEFT_FACING
        elif self.change_x > 0 and self.facing_direction == LEFT_FACING:
            self.facing_direction = RIGHT_FACING

        # idle animation
        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.facing_direction]
            return

        # jumping animation
        if self.change_y > 0:
            self.texture = self.jump_texture_pair[self.facing_direction]
            return
        elif self.change_y < 0:
            self.texture = self.idle_texture_pair[self.facing_direction]

        # walking animation
        self.cur_texture += 1
        if self.cur_texture > 7:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture][self.facing_direction]


class MainMenu(arcade.View):
    """class that manages the "menu" view"""

    def on_show(self):
        """called when switching to this view"""
        arcade.set_background_color(arcade.color.DUKE_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("(ง'̀-'́)ง Main Menu - click to play", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         color=arcade.color.OCHRE,
                         font_name='Kenney Rocket Square',
                         font_size=31, bold=True, anchor_x="center")

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        """use a mouse press to advance to the game view"""
        game_view = GameView()
        self.window.show_view(game_view)


class GameView(arcade.View):
    """main application class"""

    def __init__(self):
        """initializer"""

        super().__init__()

        # set the path to start with this program

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # take the current state of what key is pressed

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.jump_needs_reset = False

        self.tile_map = None

        # our scene
        self.scene = None

        # separate variable that hold the player sprite
        self.player_sprite = None

        # physics engine
        self.physics_engine = None

        # camera used for scrolling
        self.camera = None

        # gui elements
        self.gui_camera = None
        self.end_of_map = 0

        # self score
        self.score = 0

        # load sounds
        self.collect_coin_sound = arcade.load_sound("sounds/wining.wav")
        self.jump_sound = arcade.load_sound("sounds/jumping.wav")
        self.game_over_sound = arcade.load_sound("sounds/GameOver.wav")

    def setup(self):
        """set up the game here"""

        # cameras
        self.camera = arcade.Camera(self.window.width, self.window.height)
        self.gui_camera = arcade.Camera(self.window.width, self.window.height)

        # map name
        map_name = "platformer_game.tmj"

        # layer option
        layer_options = {
            LAYER_NAME_BACKGROUND: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_PLATFORMS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_COIN: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_MOVING_PLATFORMS: {
                "use_spatial_has": False,
            },
        }

        # map load in
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        self.score = 0

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = PlayerCharacter()
        self.player_sprite.center_x = (
                self.tile_map.tile_width * TILE_SCALING * PLAYER_START_X
        )
        self.player_sprite.center_y = (
                self.tile_map.tile_height * TILE_SCALING * PLAYER_START_Y
        )
        self.scene.add_sprite(LAYER_NAME_PLAYER, self.player_sprite)

        # Calculate the right edge of the my_map in pixels
        self.end_of_map = self.tile_map.width * GRID_PIXEL_SIZE

        # background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        # physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             platforms=self.scene[LAYER_NAME_MOVING_PLATFORMS],
                                                             gravity_constant=GRAVITY,
                                                             walls=self.scene[LAYER_NAME_PLATFORMS])

    def on_show_view(self):
        self.setup()

    def on_draw(self):
        """Render the screen"""

        # clear the screen
        self.clear()

        # activate the camera
        self.camera.use()

        # draw our scene
        self.scene.draw()

        # activate the gui camera
        self.gui_camera.use()

        # draw scores on the screen
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.BLACK, 18)

    def process_keychange(self):
        # processes left or right
        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

        if key == arcade.key.PLUS:
            self.camera.zoom(0.01)
        elif key == arcade.key.MINUS:
            self.camera.zoom(-0.01)

        self.process_keychange()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
            self.jump_needs_reset = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

        self.process_keychange()

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        self.camera.zoom(-0.01 * scroll_y)

    def center_camera_to_player(self, speed=0.2):
        screen_center_x = self.camera.scale * (self.player_sprite.center_x - (self.camera.viewport_width / 2))
        screen_center_y = self.camera.scale * (self.player_sprite.center_y - (self.camera.viewport_height / 2))
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = (screen_center_x, screen_center_y)

        self.camera.move_to(player_centered, speed)

    def on_update(self, delta_time: float):
        """movement and game logic"""

        # move the player with the physics engine
        self.physics_engine.update()

        # update animations
        if self.physics_engine.can_jump():
            self.player_sprite.can_jump = False
        else:
            self.player_sprite.can_jump = True

        # update animations
        self.scene.update_animation(
            delta_time,
            [
                LAYER_NAME_COIN,
                LAYER_NAME_BACKGROUND,
                LAYER_NAME_PLAYER,
                LAYER_NAME_GHOST,
            ],
        )

        # update moving platforms, and bullets
        self.scene.update([LAYER_NAME_MOVING_PLATFORMS, LAYER_NAME_GHOST])

        # see if enemy is hitting a boundary
        # See if the enemy hit a boundary and needs to reverse direction.
        for enemy in self.scene[LAYER_NAME_GHOST]:
            if (
                    enemy.boundary_right
                    and enemy.right > enemy.boundary_right
                    and enemy.change_x > 0
            ):
                enemy.change_x *= -1

            if (
                    enemy.boundary_left
                    and enemy.left < enemy.boundary_left
                    and enemy.change_x < 0
            ):
                enemy.change_x *= - 1

        player_collision_list = arcade.check_for_collision_with_lists(
            self.player_sprite,
            [
                self.scene[LAYER_NAME_COIN],
                self.scene[LAYER_NAME_GHOST],
            ],
        )

        # loop through each coin we hit and remove it

        for collision in player_collision_list:

            if self.scene[LAYER_NAME_GHOST] in collision.sprite_lists:
                arcade.play_sound(self.game_over_sound)
                game_over = GameOverView
                self.window.show_view(game_over)
                return
                collision.remove_from_sprite_lists()
                arcade.play_sound(self.collect_coin_sound)

        # position the camera
        self.center_camera_to_player()


class GameOverView(arcade.View):
    """class to manage the game overview"""

    def on_show_view(self):
        # called when switching to this view
        arcade.set_background_color(arcade.color.BISTRE)

    def on_draw(self):
        """Draw the game"""
        self.clear()
        arcade.draw_text("┐(シ)┌ GAME OVER - click to restart", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         color=arcade.color.OCHRE,
                         font_name='Kenney Rocket Square', )

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        """use a mouse to advance to the game view"""
        game_view = GameView()
        self.window.show_view(game_view)


def main():
    """Main function"""
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MainMenu()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
