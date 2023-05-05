# citations
# player image from: https://craftpix.net/freebies/free-monster-2d-game-items/
# bullet images and enemy sprite from: https://kenney.nl/assets/space-shooter-extension
# sound files from: https://benjaminno.itch.io/sweet-sounds-sfx-pack?download
# more in the comments

import random
import arcade

ENEMY_SCALE = 0.5
BULLET_SCALE = 0.1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Invaders"

BULLET_SPEED = 7
ENEMY_SPEED = 0.7

AMOUNT_OF_BULLET = 5

VERTICAL_MARGIN = 15
RIGHT_ENEMY_BORDER = SCREEN_WIDTH - VERTICAL_MARGIN
LEFT_ENEMY_BORDER = VERTICAL_MARGIN

# pixels enemy moving down by
ENEMY_DOWN_AMOUNT = 10

# game state
GAME_OVER = 1
PLAY_GAME = 0
# sound from zedge.net/ringtones
# original tone belongs to the show Saiki K.
game_over_sound = arcade.load_sound("sounds/game_over_sound.wav")


class InstructionView(arcade.View):

    def __init__(self):
        super().__init__()
        # create using the craftpix monster pack and background image from freepik.com
        self.texture = arcade.load_texture("images/introduction.png")
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        arcade.play_sound(game_over_sound)

    def on_draw(self):
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class GameView(arcade.View):

    def __init__(self):
        # call the parent class initializer
        super().__init__()

        # variables that hold sprite lists
        self.player_list = None
        self.enemy_list = None
        self.player_bullet_list = None
        self.enemy_bullet_list = None
        self.shield_list = None
        # enemy texture
        self.enemy_texture = None
        # set up game
        self.game_state = PLAY_GAME
        # player_info
        self.player_sprite = None
        self.score = 0
        # enemy movement
        self.enemy_change_x = -ENEMY_SPEED
        # hide the cursor
        self.window.set_mouse_visible(False)
        # sounds from itch.io
        self.hit_sound = arcade.load_sound("sounds/hit.wav")
        self.bullet_sound = arcade.load_sound("sounds/bullet.ogg")
        # sound from https://www.zedge.net/find/ringtones/
        # original sound belongs to the show One Piece
        self.kill_sound = arcade.load_sound("sounds/kill.wav")
        # background
        self.background = None

    def setup_level_one(self):
        # image from freepik.com
        self.background = arcade.load_texture("images/stars-night-textured-background.jpg")

        self.enemy_texture = []
        # image from kenney.nl
        texture = arcade.load_texture("images/enemy.png", mirrored=True)
        self.enemy_texture.append(texture)

        # create enemies
        for x in range(380, 60 * 3 + 380, 60):
            for y in range(450, 40 * 2 + 450, 40):
                # enemy image from kenney.nl
                enemy = arcade.Sprite()
                enemy.scale = ENEMY_SCALE
                enemy.texture = self.enemy_texture[0]

                # position the enemy
                enemy.center_x = x
                enemy.center_y = y

                # append to the enemy list
                self.enemy_list.append(enemy)

    def make_shield(self, x_start):

        y_start = 150
        for x in range(x_start, x_start + 25 * 6, 6):
            for y in range(y_start, y_start + 5 * 12, 12):
                shield_sprite = arcade.SpriteSolidColor(5, 12, arcade.color.BANANA_YELLOW)
                shield_sprite.center_x = x
                shield_sprite.center_y = y
                self.shield_list.append(shield_sprite)

    def setup(self):

        self.game_state = PLAY_GAME

        # sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.shield_list = arcade.SpriteList(is_static=True)

        # set up the player
        self.score = 0

        # sprite from craftpix.net
        self.player_sprite = arcade.Sprite("images/player.png", 0.2)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)

        # make the shield
        for x in range(75, 800, 200):
            self.make_shield(x)

        self.setup_level_one()

    def on_draw(self):

        # this command has to happen before we start drawing
        self.clear()

        # draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # draw all the sprites.
        self.enemy_list.draw()
        self.player_bullet_list.draw()
        self.enemy_bullet_list.draw()
        self.shield_list.draw()
        self.player_list.draw()
        # add score
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

        # game over
        if self.game_state == GAME_OVER:
            view = GameOverView()
            self.window.show_view(view)

            self.window.set_mouse_visible(True)

    def on_mouse_motion(self, x, y, dx, dy):

        if self.game_state == GAME_OVER:
            return
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):

        if len(self.player_bullet_list) < AMOUNT_OF_BULLET:
            # bullet sound
            arcade.play_sound(self.bullet_sound)

            # Create a bullet
            # image from kenney.nl
            bullet = arcade.Sprite("images/player_bullet.png", BULLET_SCALE)

            # add speed
            bullet.change_y = BULLET_SPEED

            # position the bullet
            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top

            # append to the list
            self.player_bullet_list.append(bullet)

    def update_enemies(self):

        # move the enemy up and down
        for enemy in self.enemy_list:
            enemy.center_x += self.enemy_change_x

        move_down = False
        for enemy in self.enemy_list:
            if enemy.right > RIGHT_ENEMY_BORDER and self.enemy_change_x > 0:
                self.enemy_change_x *= -1
                move_down = True
            if enemy.left < LEFT_ENEMY_BORDER and self.enemy_change_x < 0:
                self.enemy_change_x *= -1
                move_down = True

        if move_down:
            for enemy in self.enemy_list:
                # move the enemy down
                enemy.center_y -= ENEMY_DOWN_AMOUNT

    def allow_enemies_to_fire(self):

        fire = []
        for enemy in self.enemy_list:
            chance = 9 + len(self.enemy_list) * 6
            if random.randrange(chance) == 0 and enemy.center_x not in fire:
                # image from kenney.nl
                bullet = arcade.Sprite("images/enemy_bullet.png", 0.7)
                # change the angle
                bullet.angle = 180
                # set the speed
                bullet.change_y = -BULLET_SPEED
                # position
                bullet.center_x = enemy.center_x
                bullet.top = enemy.bottom
                self.enemy_bullet_list.append(bullet)
            # add to the list
            fire.append(enemy.center_x)

    def process_enemy_bullets(self):

        # Move the bullets
        self.enemy_bullet_list.update()
        # Loop through each bullet
        for bullet in self.enemy_bullet_list:
            # check for collision with shield area
            hit_list = arcade.check_for_collision_with_list(bullet, self.shield_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                for shield in hit_list:
                    shield.remove_from_sprite_lists()
                continue
            if arcade.check_for_collision_with_list(self.player_sprite, self.enemy_bullet_list):
                arcade.play_sound(self.kill_sound)
                self.game_state = GAME_OVER

            # get rid of any bullet that flies off the screen
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

    def process_player_bullets(self):

        self.player_bullet_list.update()

        # Loop through each bullet
        for bullet in self.player_bullet_list:

            # check if a bullet hit the shield
            hit_list = arcade.check_for_collision_with_list(bullet, self.shield_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                for shield in hit_list:
                    shield.remove_from_sprite_lists()
                continue
            # check if a bullet hit an enemy
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # remove the enemy and add to the score
            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.hit_sound)

            # remove any bullets that fly off the screen
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

    def on_update(self, delta_time):

        if self.game_state == GAME_OVER:
            return

        self.update_enemies()
        self.allow_enemies_to_fire()
        self.process_enemy_bullets()
        self.process_player_bullets()

        if len(self.enemy_list) == 0:
            self.setup_level_one()


class GameOverView(arcade.View):

    def __init__(self):
        super().__init__()
        # image created from freepik.com and craftpik monster pack.
        self.texture = arcade.load_texture("images/game_over.png")
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
