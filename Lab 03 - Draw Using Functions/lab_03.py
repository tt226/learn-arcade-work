import arcade
import math
import random

arcade.open_window(1000, 800)

arcade.set_background_color(arcade.color.DARK_SLATE_BLUE)

arcade.start_render()

arcade.draw_circle_filled(550, 734, 50, arcade.color.INDIAN_YELLOW)

def draw_building(x, y):
    arcade.draw_rectangle_filled(x, y, 140, 530, arcade.color.BLACK)
    arcade.draw_rectangle_outline(x, y, 140, 530, arcade.color.GRAY_BLUE, 9)
    arcade.draw_rectangle_outline(x, y, 140, 530, arcade.color.SLATE_GRAY, 2)


def draw_window(x, y, c):
    arcade.draw_rectangle_outline(x, y, 90, 44, arcade.color.DIM_GRAY, 2)
    arcade.draw_rectangle_filled(x, y, 90, 44, c)


draw_building(768, 431)
draw_window(768, 310, arcade.color.PALE_VIOLET_RED)
draw_window(768, 390, arcade.color.PALE_VIOLET_RED)
draw_window(768, 470, arcade.color.PALE_VIOLET_RED)
draw_window(768, 550, arcade.color.PALE_VIOLET_RED)
draw_window(768, 630, arcade.color.PALE_VIOLET_RED)


draw_building(410, 340)
draw_building(210, 340)
draw_building(310, 432)
draw_building(555, 222)


draw_window(310, 320, arcade.color.DEEP_LEMON)
draw_window(310, 400, arcade.color.DEEP_LEMON)
draw_window(310, 480, arcade.color.DEEP_LEMON)
draw_window(310, 565, arcade.color.DEEP_LEMON)
draw_window(310, 650, arcade.color.DEEP_LEMON)

draw_building(650, 410)
draw_window(648, 310, arcade.color.PINK_LAVENDER)
draw_window(648, 390, arcade.color.PINK_LAVENDER)
draw_window(648, 470, arcade.color.PINK_LAVENDER)
draw_window(648, 550, arcade.color.PINK_LAVENDER)
draw_window(648, 630, arcade.color.PINK_LAVENDER)

draw_building(90, 510)
draw_window(90, 310, arcade.color.LIGHT_SKY_BLUE)
draw_window(90, 390, arcade.color.LIGHT_SKY_BLUE)
draw_window(90, 470, arcade.color.LIGHT_SKY_BLUE)
draw_window(90, 550, arcade.color.LIGHT_SKY_BLUE)
draw_window(90, 630, arcade.color.LIGHT_SKY_BLUE)
draw_window(90, 710, arcade.color.LIGHT_SKY_BLUE)


draw_building(450, 510)
draw_window(450, 710, arcade.color.LIVER)
draw_window(450, 630, arcade.color.LIVER)
draw_window(450, 550, arcade.color.LIVER)
draw_window(450, 470, arcade.color.LIVER)
draw_window(450, 385, arcade.color.LIVER)
draw_window(450, 300, arcade.color.LIVER)

draw_building(910, 210)
draw_window(910, 420, arcade.color.NAPIER_GREEN)
draw_window(910, 330, arcade.color.NAPIER_GREEN)
draw_window(910, 250, arcade.color.NAPIER_GREEN)

def draw_flower(x, y, z, m):
    arcade.draw_ellipse_outline(x, y, 120, 40, z, 80, 38)
    arcade.draw_ellipse_outline(x, y, 120, 40, z, 80, 78)
    arcade.draw_circle_filled(x, y, 18, m, 23)

arcade.draw_lrtb_rectangle_filled(0, 999, 240, 0, arcade.color.DARK_SLATE_GRAY)

draw_flower(60, 60, arcade.color.PASTEL_VIOLET, arcade.color.PAPAYA_WHIP)
draw_flower(150, 60, arcade.color.RHYTHM, arcade.color.STORMCLOUD)
draw_flower(950, 100, arcade.color.PINK_SHERBET, arcade.color.STORMCLOUD)
draw_flower(350, 100, arcade.color.DEEP_LEMON, arcade.color.PAPAYA_WHIP)
draw_flower(260, 60, arcade.color.PASTEL_VIOLET, arcade.color.PAPAYA_WHIP)
draw_flower(850, 100, arcade.color.PINK_SHERBET, arcade.color.STORMCLOUD)
draw_flower(450, 100, arcade.color.DEEP_LEMON, arcade.color.PAPAYA_WHIP)
draw_flower(900, 100, arcade.color.DEEP_LEMON, arcade.color.PAPAYA_WHIP)
draw_flower(360, 60, arcade.color.PASTEL_VIOLET, arcade.color.PAPAYA_WHIP)
draw_flower(820, 100, arcade.color.DEEP_LEMON, arcade.color.PAPAYA_WHIP)
draw_flower(560, 60, arcade.color.PASTEL_VIOLET, arcade.color.PAPAYA_WHIP)

arcade.draw_lrtb_rectangle_filled(0, 999, 260, 240, arcade.color.SNOW)


arcade.finish_render()

arcade.run()
