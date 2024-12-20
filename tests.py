import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_create_cells_with_margin(self):
        num_cols = 30
        num_rows = 20
        m1 = Maze(10, 10, num_rows, num_cols, 15, 15, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertFalse(m1._cells[0][0].has_left_wall)
        self.assertFalse(m1._cells[-1][-1].has_bottom_wall)

    def test_resetted_visited_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        for row in m1._cells:
            for cell in row:
                self.assertFalse(cell.visited)
        
if __name__ == "__main__":
    unittest.main()