import arcade
import math

arcade.open_window(800, 600)

arcade.set_background_color((112, 128, 144))

arcade.start_render()

Screen_Width = 600
Screen_HEIGHT = 600

arcade.draw_lrtb_rectangle_filled(0, 400, 800, 0, arcade.csscolor.ROSY_BROWN)

# Draw a smiley face

arcade.draw_circle_filled(Screen_Width / 4, Screen_HEIGHT / 2, 50, arcade.color.INDIAN_YELLOW)

# Left eye
x = 130
y = 310
arcade.draw_circle_filled(x, y, 7, arcade. color .LIGHT_BROWN)

# Right eye
x = 170
y = 310
arcade.draw_circle_filled(x, y, 7, arcade. color .LIGHT_BROWN)

# Draw the eyebrows
arcade.draw_arc_filled(168, 325, 20, 10, arcade.color.LIGHT_BROWN, 350, 580, 3)
arcade.draw_arc_filled(130, 325, 18, 10, arcade.color.LIGHT_BROWN, 340, 560, 3)

# Draw the smile
x = 150
y = 300
width = 43
height = 55
start_angle = 240
end_angle = 320
arcade.draw_arc_outline(x, y, width, height, arcade.color.LIGHT_BROWN, start_angle, end_angle,9)

arcade.draw_triangle_filled(200, 400, 190, 340, 190, 340, arcade.csscolor.DARK_GREEN)


# Right Smile

arcade.draw_circle_filled(Screen_Width / 1, Screen_HEIGHT / 2, 50, arcade.color.INDIAN_YELLOW)

# Draw the eyes

# Left eye
x = 580
y = 310
arcade.draw_circle_filled(x, y, 7, arcade. color .LIGHT_BROWN)

# Right eye
x = 620
y = 310
arcade.draw_circle_filled(x, y, 7, arcade. color .LIGHT_BROWN)

# Draw the eyebrows
arcade.draw_arc_filled(620, 325, 20, 10, arcade.color.LIGHT_BROWN, 350, 580, 3)
arcade.draw_arc_filled(580, 325, 20, 10, arcade.color.LIGHT_BROWN, 320, 550, 3)

# Draw the smile
x = 600
y = 280
width = 18
height = 10
start_angle = 340
end_angle = 560
arcade.draw_arc_filled(600, 280, 18, 10, arcade.color.LIGHT_BROWN, 340, 560, 3)



arcade.finish_render()

arcade.run()
