""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


class Building:

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
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width - 2, self.height - 2,
                                     arcade.color.PINK_PEARL)
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width - 3, self.height - 3,
                                     arcade.color.PINK_SHERBET)
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width - 5, self.height / -5,
                                     arcade.color.PAPAYA_WHIP)
        arcade.draw_rectangle_filled(self.position_x, self.position_y, 90, 44, arcade.color.BLUEBERRY)
        arcade.draw_text("OPEN", start_x=340, color=arcade.color.OCHRE, start_y=410, font_name="Kenney Rocket Square",
                         font_size=45, bold=True)
        arcade.draw_circle_filled(130, 500, 60, arcade.color.INDIAN_YELLOW)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        arcade.set_background_color(arcade.color.BLACK)
        self.building = Building(610, 140, 210, 530, arcade.color.AMBER, 0, 0)
        self.window = Building(390, 140, 210, 530, arcade.color.AIR_FORCE_BLUE, 0, 0)

    def on_draw(self):
        arcade.start_render()
        self.building.draw()
        self.window.draw()

    def update(self, delta_time):
        self.building.update()
        self.window.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.building.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.building.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.building.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.building.change_y = -MOVEMENT_SPEED


def main():
    window = MyGame()

    arcade.run()


main()
