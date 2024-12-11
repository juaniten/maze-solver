from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point_1, point_2):
        self._point_1 = point_1
        self._point_2 = point_2

    def draw(self, canvas, fill_color):
        DEFAULT_WIDTH = 2
        canvas.create_line(self._point_1.x, self._point_1.y, 
                           self._point_2.x, self._point_2.y,
                           fill=fill_color, width = DEFAULT_WIDTH)

class Window():
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
        self._root = Tk()
        self._root.title = "Maze solver"
        self._root.protocol("WM_DELETE_WINDOW", self.close)

        self._canvas = Canvas(self._root, height=self._height, width=self._width)
        self._canvas.pack()
        self._window_running = False
        

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._window_running = True
        while self._window_running:
            self.redraw()

    def close(self):
        self._window_running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self._canvas, fill_color)


class Cell():
    def __init__(self, upper_left: Point, lower_right: Point, window: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._upper_left = upper_left
        self._lower_right = lower_right
        self._upper_right = Point(lower_right.x, upper_left.y)
        self._lower_left = Point(upper_left.x, lower_right.y)
        
        self.center = Point(self._upper_right.x - (self._upper_right.x - self._upper_left.x) / 2, 
                            self._lower_left.y - (self._lower_left.y - self._upper_left.y) / 2)
        self._window = window
        self.visited = False

    def draw(self):
        if self._window is None:
            return
        DEFAULT_FILL_COLOR = "black"
        DEFAULT_BACKGROUND_COLOR = "#d9d9d9"
        if self.has_left_wall:
            self._window.draw_line(Line(self._upper_left, self._lower_left), DEFAULT_FILL_COLOR)
        else:
            self._window.draw_line(Line(self._upper_left, self._lower_left), DEFAULT_BACKGROUND_COLOR)

        if self.has_right_wall:
            self._window.draw_line(Line(self._upper_right, self._lower_right), DEFAULT_FILL_COLOR)
        else:
            self._window.draw_line(Line(self._upper_right, self._lower_right), DEFAULT_BACKGROUND_COLOR)
        if self.has_top_wall:
            self._window.draw_line(Line(self._upper_left, self._upper_right), DEFAULT_FILL_COLOR)
        else:
            self._window.draw_line(Line(self._upper_left, self._upper_right), DEFAULT_BACKGROUND_COLOR)
        if self.has_bottom_wall:
            self._window.draw_line(Line(self._lower_left, self._lower_right), DEFAULT_FILL_COLOR)
        else:
            self._window.draw_line(Line(self._lower_left, self._lower_right), DEFAULT_BACKGROUND_COLOR)

    def draw_move(self, to_cell, undo=False):
        line_color = "gray" if undo else "red"

        line = Line(self.center, to_cell.center)
        self._window.draw_line(line, line_color)
        