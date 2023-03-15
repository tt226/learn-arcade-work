""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Building():

    def __init__(self, position_x, position_y, width, height, color, change_x, change_y):
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.color = color
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width/2, self.height/2, arcade.color.DARK_ORANGE)


    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        arcade.set_background_color(arcade.color.BLACK_BEAN)

        self.building = Building(410, 140, 200, 530, arcade.color.MINT_CREAM, 2, 4)


    def on_draw(self):
        arcade.start_render()
        self.building.draw()


    def update(self, delta_time):
        self.building.update()


def main():
    window = MyGame()
    arcade.run()


main()
