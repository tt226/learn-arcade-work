import arcade

# Draw a cat
# each point will be a pixel so 800 pixel wide, will have x-coordinates that run from 0 to 799
arcade.open_window(600, 600, "Tayyaba's cat")

# set a background color
arcade.set_background_color(arcade.color.ROSE_BONBON)

# get ready to draw
arcade.start_render()

# draw a green field
arcade.draw_rectangle_filled(300, 120, 600, 300, arcade.color.YELLOW_ORANGE)
# finish drawing
arcade.finish_render()

# keep the window up until someone closes it.
arcade.run()
