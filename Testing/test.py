import arcade
import math

arcade.open_window(800, 800)

arcade.set_background_color((112, 128, 144))

arcade.start_render()

Screen_Width = 800
Screen_HEIGHT = 800

arcade.draw_lrtb_rectangle_filled(200, 400, 300, 0, arcade.color.PINK)
arcade.draw_rectangle_filled(200, 400, 30, 28, arcade.color.BLUE_VIOLET)
arcade.draw_circle_filled(700, 700, 45, arcade.color.BLACK)
arcade.draw_ellipse_outline(600,600, 25, 50, arcade.color. PAPAYA_WHIP, 80, 190)
# Tree
arcade.draw_rectangle_filled(200, 300, 20, 60, arcade.csscolor.INDIANRED)
arcade.draw_ellipse_filled(200, 350, 50, 100, arcade.csscolor.STEEL_BLUE)

arcade.draw_arc_filled(400, 400, 100, 100, arcade.color.OLD_ROSE, 0, 180, 100)

# TRIANGLE
arcade.draw_triangle_filled(600, 600, 535, 535, 635, 535, arcade.csscolor.DARK_RED)

arcade.draw_polygon_filled(((740, 730), (750, 730), (740, 740), (750, 740), (760, 735)), arcade.color.GOLD)

arcade.draw_line(100, 100, 400, 400, arcade.color. YELLOW_ROSE, 8)

arcade.draw_text("Win for us - Seventeenth!", 300, 450, arcade.color.PINK, 130)

arcade.finish_render()

arcade.run()

