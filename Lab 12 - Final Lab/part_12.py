# itch.io - Pixel Adventure - https://pixelfrog-assets.itch.io/pixel-adventure-1
# https://benjaminno.itch.io/sweet-sounds-sfx-pack?download
# https://kenney.nl/assets/alien-ufo-pack

# source code - citations
# platform_tutorial
# https://api.arcade.academy/en/latest/examples/platform_tutorial/step_17.html
# Maze depth first
# https://api.arcade.academy/en/development/example_code/how_to_examples/maze_depth_first.html


import random
import arcade
import timeit

NORMAL_SPRITE_SIZE = 190
SPRITE_SCALING = 0.25
SPRITE_SIZE = int(NORMAL_SPRITE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Mazes"
MOVEMENT_SPEED = 4
TILE_EMPTY = 0
TILE_CRATE = 1
FROG_WALK_SPEED = 0.8

MAZE_HEIGHT = 35
MAZE_WIDTH = 35

MERGE_SPRITES = True

VIEWPORT_MARGIN = 200

# sounds from ich.io - "Sweet Sounds - by Coffee Bat
# https://benjaminno.itch.io/sweet-sounds-sfx-pack?download

coinn_sound = arcade.load_sound("assets/sounds/jumping.wav")
game_over = arcade.load_sound("assets/sounds/GameOver.wav")


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        # coin position
        self.center_x = random.randrange(SCREEN_HEIGHT)
        self.center_y = random.randrange(SCREEN_WIDTH)
        # change in position
        self.change_x += 5
        self.change_y += 5

    def update(self):
        self.center_y += self.center_x
        self.center_y += self.change_y


class Frog(arcade.Sprite):
    def __init__(self, filename):
        super(Frog, self).__init__(filename, 1.2)
        self.frog_sprite = None
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.center_y = 0

    # update position
    def update(self):
        self.center_x += self.center_x
        self.center_y += self.center_y

    def follow_sprite(self, player_sprite):
        """move the sprite towards the other sprite"""

        if self.center_y < player_sprite.center_y:
            self.center_y += min(FROG_WALK_SPEED, player_sprite.center_y - self.center_y)

        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(FROG_WALK_SPEED, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(FROG_WALK_SPEED, player_sprite.center_x - self.center_x)

        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(FROG_WALK_SPEED, self.center_x - player_sprite.center_x)


def _create_grid_with_cells(width, height):
    # Create a grid with empty cells on odd row/column combinations.
    grid = []
    for row in range(height):
        grid.append([])
        for column in range(width):
            if column % 2 == 1 and row % 2 == 1:
                grid[row].append(TILE_EMPTY)
            elif column == 0 or row == 0 or column == width - 1 or row == height - 1:
                grid[row].append(TILE_CRATE)
            else:
                grid[row].append(TILE_CRATE)
    return grid


def make_maze_depth_first(maze_width, maze_height):
    maze = _create_grid_with_cells(maze_width, maze_height)

    w = (len(maze[0]) - 1) // 2
    h = (len(maze) - 1) // 2
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]

    def walk(x: int, y: int):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        random.shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                maze[max(y, yy) * 2][x * 2 + 1] = TILE_EMPTY
            if yy == y:
                maze[y * 2 + 1][max(x, xx) * 2] = TILE_EMPTY

            walk(xx, yy)

    walk(random.randrange(w), random.randrange(h))

    return maze


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None
        self.frog_list = None

        # Player info
        self.score = 0
        self.player_sprite = None

        # Physics engine
        self.physics_engine = None

        # Used to scroll
        self.view_bottom = 0
        self.view_left = 0

        # Time to process
        self.processing_time = 0
        self.draw_time = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.frog_list = arcade.SpriteList()

        self.score = 0

        # Create the maze
        maze = make_maze_depth_first(MAZE_WIDTH, MAZE_HEIGHT)

        # Create sprites based on 2D grid
        if not MERGE_SPRITES:
            # each grid is a sprite.
            for row in range(MAZE_HEIGHT):
                for column in range(MAZE_WIDTH):
                    if maze[row][column] == 1:
                        # itch.io - Pixel Adventure - https://pixelfrog-assets.itch.io/pixel-adventure-1
                        wall = arcade.Sprite("gray.png", scale=SPRITE_SCALING)
                        wall.center_x = column * SPRITE_SIZE + SPRITE_SIZE / 2
                        wall.center_y = row * SPRITE_SIZE + SPRITE_SIZE / 2
                        self.wall_list.append(wall)
        else:
            for row in range(MAZE_HEIGHT):
                column = 0
                while column < len(maze):
                    while column < len(maze) and maze[row][column] == 0:
                        column += 1
                    start_column = column
                    while column < len(maze) and maze[row][column] == 1:
                        column += 1
                    end_column = column - 1

                    column_count = end_column - start_column + 1
                    column_mid = (start_column + end_column) / 2
                    # itch.io - Pixel Adventure - https://pixelfrog-assets.itch.io/pixel-adventure-1
                    wall = arcade.Sprite("new/Purple.png", scale=SPRITE_SCALING)
                    wall.center_x = column_mid * SPRITE_SIZE + SPRITE_SIZE / 2
                    wall.center_y = row * SPRITE_SIZE + SPRITE_SIZE / 2
                    wall.width = SPRITE_SIZE * column_count
                    self.wall_list.append(wall)

        # Set up the player
        self.player_sprite = arcade.Sprite(
            # kenney's UFO pack - https://kenney.nl/assets/alien-ufo-pack
            "new/shipYellow_manned.png",
            scale=SPRITE_SCALING)
        self.player_list.append(self.player_sprite)

        # randomly place the player
        placed = False
        while not placed:

            # Randomly position
            self.player_sprite.center_x = random.randrange(MAZE_WIDTH * SPRITE_SIZE)
            self.player_sprite.center_y = random.randrange(MAZE_HEIGHT * SPRITE_SIZE)

            # Are we in a wall?
            walls_hit = arcade.check_for_collision_with_list(self.player_sprite, self.wall_list)
            if len(walls_hit) == 0:
                # Not in a wall! Success!
                placed = True

            # coin placed successfully
            for coin in range(80):
                # itch.io - Pixel Adventure - https://pixelfrog-assets.itch.io/pixel-adventure-1
                coin = Coin("new/tile000.png", 0.8)
                coin_placed_right = False
                while not coin_placed_right:
                    coin.center_x = random.randrange(SCREEN_WIDTH)
                    coin.center_y = random.randrange(SCREEN_HEIGHT)
                    # checking for collision
                    coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)
                    frog_list = arcade.check_for_collision_with_list(coin, self.frog_list)
                    wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
                    if len(frog_list) == 0 and len(coin_hit_list) == 0 and len(wall_hit_list) == 0:
                        coin_placed_right = True
                        # add
                        self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        self.background_color = arcade.color.JUNGLE_GREEN

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """
        # display score
        # Put the text on the screen.
        output = f"SCORE: {self.score}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 60 + self.view_bottom,
                         arcade.color.WHITE, 16)

        self.clear()

        # Start timing how long this takes
        draw_start_time = timeit.default_timer()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        self.frog_list.draw()

        sprite_count = len(self.wall_list)

        output = f"Sprite Count: {sprite_count}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 20 + self.view_bottom,
                         arcade.color.WHITE, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 40 + self.view_bottom,
                         arcade.color.WHITE, 16)

        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 60 + self.view_bottom,
                         arcade.color.WHITE, 16)

        self.draw_time = timeit.default_timer() - draw_start_time

        # frog
        frog_sprite = Frog("new/walk.png")
        # position
        frog_sprite.change_x = 200
        frog_sprite.center_x = 100
        frog_sprite.change_x += 2.88
        # Score Board
        output = f"Score : {self.score:.3f}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 80 + self.view_bottom,
                         arcade.color.WHITE, 16)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time, start_time=None):
        """ Movement and game logic """
        for frog in self.frog_list:
            frog.follow_sprite(self.player_sprite)

        # sprites that connect with each other
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(coinn_sound)

        not_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.frog_list)
        for frog in not_hit_list:
            frog.remove_from_sprite_lists()
            self.score -= 1
            arcade.draw_rectangle_filled(SCREEN_WIDTH, SCREEN_HEIGHT, 90, 44, arcade.color.CYBER_GRAPE)
            arcade.play_sound(game_over)
        # Call update on all sprites
        self.physics_engine.update()
        # Track if we need to change the viewport
        changed = False

        # Scroll left
        left_side = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_side:
            self.view_left -= left_side - self.player_sprite.left
            changed = True

        # Scroll right
        right_side = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_side:
            self.view_left += self.player_sprite.right - right_side
            changed = True

        # Scroll up
        top_side = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_side:
            self.view_bottom += self.player_sprite.top - top_side
            changed = True

        # Scroll down
        top_side = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < top_side:
            self.view_bottom -= top_side - self.player_sprite.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        if self.score >= 20:
            self.clear()
            arcade.draw_text("GAME OVER", start_x=140, color=arcade.color.OCHRE, start_y=350,
                             font_name="Kenney Rocket Square",
                             font_size=50, bold=True)

        if self.score <= 20:
            self.clear()
            arcade.draw_text("YOU LOST \n ¯\_(ツ)_/¯", start_x=210, color=arcade.color.OCHRE, start_y=240,
                             font_name="Kenney Rocket Square",
                             font_size=20, bold=True)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
