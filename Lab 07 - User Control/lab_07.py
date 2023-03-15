""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


class Sun():
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < self.radius:
            self.position_x = self.radius
        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
        if self.position_y > SCREEN_WIDTH - self.radius:
            self.position_y = SCREEN_WIDTH - self.radius


class Ring():

    def __init__(self, position_x, position_y, color):
        self.position_x = position_x
        self.position_y = position_y
        self.color = color

    def on_draw(self):
        arcade.draw_ellipse_outline(self.position_x, self.position_y, 100, 50, self.color, 3)
        arcade.draw_ellipse_outline(self.position_x, self.position_y, 50, 100, arcade.color.OCHRE, 3)
        arcade.draw_circle_filled(self.position_x, self.position_y, 13, arcade.color.PINK_SHERBET, 23)


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
        arcade.draw_text("(►.◄)", start_x=320, color=arcade.color.OCHRE, start_y=410,
                         font_name="Kenney Rocket Square",
                         font_size=45, bold=True)
        arcade.draw_text("(►.◄)", start_x=540, color=arcade.color.OCHRE, start_y=410, font_name="Kenney Rocket Square",
                         font_size=45, bold=True)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        arcade.set_background_color(arcade.color.BLACK)
        self.building = Building(610, 140, 210, 530, arcade.color.AMBER, 0, 0)
        self.window = Building(390, 140, 210, 530, arcade.color.AIR_FORCE_BLUE, 0, 0)
        self.sun = Sun(120, 510, 0, 0, 60, arcade.color.INDIAN_YELLOW)
        self.ring = Ring(120, 510, arcade.color.OCHRE)

    def on_draw(self):
        arcade.start_render()
        self.building.draw()
        self.window.draw()
        self.sun.draw()
        self.ring.on_draw()

    def update(self, delta_time):
        self.sun.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.sun.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.sun.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.sun.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.sun.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.sun.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.sun.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
