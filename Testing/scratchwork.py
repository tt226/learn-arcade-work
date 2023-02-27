import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.OLD_ROSE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.PINK)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.APPLE_GREEN)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.FLORAL_WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.PURPLE_HEART)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.PURPLE_HEART)




def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_snow_person(on_draw.snow_person1_x, 140)
    draw_snow_person(450, 180)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.snow_person1_x += 1


# Create a value that our on_draw.snow_person1_x will start at.
on_draw.snow_person1_x = 150


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLUEBERRY)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()


# Call the main function to get the program started.
main()


import random
num = random.random()
print(num)


num = random.randint(10, 20)
print(num)

num = random.randrange(112, 320, 2)
print(num)

num = random.uniform(50, 70)
print(num)

numList = random.sample(range(120, 139), 8)
print(numList)

numList = [1,2,3,4,5]
random.shuffle(numList)
print(numList)
print(random.choice(numList))