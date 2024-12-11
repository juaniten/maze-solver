import time

from graphics import Point, Cell, Window

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Window,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for x in range(self._x1, self._num_cols * self._cell_size_x, self._cell_size_x):
            self._cells.append([])
            for y in range(self._y1, self._num_rows * self._cell_size_y, self._cell_size_y):
                new_cell = Cell(Point(x, y),
                                Point(x + self._cell_size_x, y + self._cell_size_y),
                                self._win)
                self._cells[-1].append(new_cell)
                new_cell.draw()
                self._animate()

                
                

    def _animate(self):
        self._win.redraw()
        # time.sleep(0.05)