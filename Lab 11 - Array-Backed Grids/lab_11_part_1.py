import arcade

# set how many rows and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10

# this sets width and height of each grid location
WIDTH = 20
HEIGHT = 20

# this sets the margin between each sell
# and on the edges of the screen
MARGIN = 5

# Screen dimension math
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main Application class.
    """

    def __init__(self, width, height):

        """
        Set up the application
        """
        super().__init__(width, height)
        # create a two-dimensional array; simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an array that will hold each cell in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

            self.background_color = arcade.color.BLACK

    def on_draw(self):

        """
        Render the screen
        """

        # this command has to happen before we start drawing
        arcade.start_render()

        # draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        """
        Called when the user presses a mouse button
        """

        # change the x/y coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({column}, {row})")

        # making sure we are on-grid
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0
        # change the color of the surrounding boxes
        if (row + 1) < ROW_COUNT:
            if self.grid[row + 1][column] == 0:
                self.grid[row + 1][column] = 1
            else:
                self.grid[row + 1][column] = 0

        if (row - 1) < ROW_COUNT:
            if self.grid[row - 1][column] == 0:
                self.grid[row - 1][column] = 1
            else:
                self.grid[row - 1][column] = 0

        if (column + 1) < COLUMN_COUNT:
            if self.grid[row][column + 1] == 0:
                self.grid[row][column + 1] = 1
            else:
                self.grid[row][column + 1] = 0

        if (column + 1) > COLUMN_COUNT:
            if self.grid[row][column + 1] == 0:
                self.grid[row][column - 1] = 1
            else:
                self.grid[row][column + 1] = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
