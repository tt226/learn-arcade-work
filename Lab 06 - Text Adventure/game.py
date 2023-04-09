import arcade
import random

# variables

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SPEED = 120

arcade.open_window(900, 600, "Gaming project")

arcade.start_render()

arcade.set_background_color(arcade.color.BLANCHED_ALMOND)
star = arcade.Sprite("star.png")

def update():
    arcade.Sprite("star.png", SPEED)


def stars():
    for i in range(5):
        for column in range(30):
            i = 2 * 1


arcade.finish_render()

arcade.run()
