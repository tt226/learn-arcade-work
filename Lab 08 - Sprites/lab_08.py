""" Sprite Sample Program """
import arcade
import random

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.4
SPRITE_SCALING_LASER = 0.4
COIN_COUNT = 55
LASER_COUNT = 25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

lose_sound = arcade.load_sound("zapp1.wav")
win_sound = arcade.load_sound("power_rup.wav")


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

    def reset_position(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 10, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1

        if self.top < 0:
            self.reset_position()



class Laser(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_y *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # variables that will hold sprite lists.
        self.player_list = None
        self.coin_list = None
        self.laser_list = None

        # player info
        self.player_sprite = None
        self.score = 0
        self.game_over = False

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.RICH_BLACK)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()

        # score
        self.score = 0

        # characters
        self.player_sprite = arcade.Sprite("green_spaceship.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        # add
        self.player_list.append(self.player_sprite)

        # yellow gem
        for i in range(COIN_COUNT):
            coin = Coin("yellow_ball.png", SPRITE_SCALING_COIN / 3)
            # position the coins
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # add
            self.coin_list.append(coin)

        # laser
        for i in range(LASER_COUNT):
            laser = Laser("laser_beam.png", SPRITE_SCALING_LASER)
            # position the coins
            laser.center_x = random.randrange(120, SCREEN_WIDTH)
            laser.center_y = random.randrange(SCREEN_HEIGHT)
            laser.change_x = random.randrange(-3, 4)
            laser.change_y = random.randrange(-3, 4)

            # add
            self.laser_list.append(laser)

    def on_draw(self):
        # Draw everything
        arcade.start_render()
        self.player_list.draw()
        self.coin_list.draw()
        self.laser_list.draw()

        if self.game_over:
            arcade.draw_text("GAME OVER", start_x=140, color=arcade.color.OCHRE, start_y=350,
                             font_name="Kenney Rocket Square",
                             font_size=50, bold=True)

            if self.score <= 50:
                arcade.draw_text("YOU LOST \n ¯\_(ツ)_/¯", start_x=210, color=arcade.color.OCHRE, start_y=240,
                                 font_name="Kenney Rocket Square",
                                 font_size=20, bold=True)

            if self.score == 50:
                arcade.draw_text("YOU WON"
                                 '°˖✧◝(⁰▿⁰)◜✧˖°', start_x=330, color=arcade.color.OCHRE, start_y=240,
                                 font_name="Kenney Rocket Square",
                                 font_size=20, bold=True)

        output = f"Score:  {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.PAPAYA_WHIP, 14)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        # mouse motion
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        # score board
        self.coin_list.update()
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(win_sound)

        self.laser_list.update()
        laser_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.laser_list)
        for laser in laser_hit_list:
            laser.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(lose_sound)

        if len(self.coin_list) == 0:
            self.game_over = True
            self.coin_list.clear()
            self.player_list.clear()
            self.laser_list.clear()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
