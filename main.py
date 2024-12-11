from graphics import Window, Line, Point, Cell
from maze import Maze

def main() -> None:

    margin = 10
    num_cols = 18
    num_rows = 12

    cell_width = 40
    cell_height = 40

    window_width = margin * 2 + cell_width * num_cols
    window_height = margin * 2 + cell_height * num_rows

    win = Window(window_width, window_height)

    maze = Maze(margin, margin, num_rows, num_cols, cell_width, cell_height, win)

    win.wait_for_close()



if __name__ == '__main__':
    main()