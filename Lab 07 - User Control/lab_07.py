""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Emoji:
    def __init__(self, position_x, position_y, radius, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def draw_flower(x, y, z, m):
        arcade.draw_ellipse_outline(x, y, 120, 40, z, 80, 38)
        arcade.draw_ellipse_outline(x, y, 120, 40, z, 80, 78)
        arcade.draw_circle_filled(x, y, 18, m, 23)

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

    def on_draw(self):
        arcade.start_render()


def main():
    window = MyGame()
    arcade.run()

main()
