import arcade
import math
import turtle

arcade.open_window(800, 600)

arcade.set_background_color((112, 128, 144))

arcade.start_render()

Screen_Width = 600
Screen_HEIGHT = 600
texture = arcade.load_texture("emoticon-2120024__340.png")
arcade.finish_render()
arcade.run()