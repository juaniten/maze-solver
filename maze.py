import time
import random
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
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        random.seed(seed) if seed is not None else random.seed()

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

        self._break_walls_r(0,0)
        self._reset_cells_visited()


    def _create_cells(self):
        for x in range(self._x1, self._num_cols * self._cell_size_x + self._x1, self._cell_size_x):
            self._cells.append([])
            for y in range(self._y1, self._num_rows * self._cell_size_y + self._y1, self._cell_size_y):
                new_cell = Cell(Point(x, y),
                                Point(x + self._cell_size_x, y + self._cell_size_y),
                                self._win)
                self._cells[-1].append(new_cell)
                new_cell.draw()
                
    def _animate(self):
        self._win.redraw()
        time.sleep(0.03)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[0][0].draw()
        self._cells[-1][-1].has_bottom_wall = False
        self._cells[-1][-1].draw()

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            if i - 1 >= 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if i + 1 <= len(self._cells) - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j - 1 >= 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j + 1 <= len(self._cells[0]) - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
        
            if len(to_visit) == 0:
                current_cell.draw()
                return
            
            (chosen_i, chosen_j) = to_visit[random.randrange(0, len(to_visit))]
            chosen_cell = self._cells[chosen_i][chosen_j]
            
            if chosen_i == i - 1: # left
                current_cell.has_left_wall = False
                chosen_cell.has_right_wall = False
            if chosen_i == i + 1: # right
                current_cell.has_right_wall = False
                chosen_cell.has_left_wall = False
            if chosen_j == j - 1: # top
                current_cell.has_top_wall = False
                chosen_cell.has_bottom_wall = False
            if chosen_j == j + 1: # bottom
                current_cell.has_bottom_wall = False
                chosen_cell.has_top_wall = False

            self._break_walls_r(chosen_i, chosen_j)
                
    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True
        
        to_visit = []
        if i - 1 >= 0 and not self._cells[i - 1][j].visited and not current_cell.has_left_wall:
            to_visit.append((i - 1, j))
        if i + 1 <= len(self._cells) - 1 and not self._cells[i + 1][j].visited and not current_cell.has_right_wall:
            to_visit.append((i + 1, j))
        if j - 1 >= 0 and not self._cells[i][j - 1].visited and not current_cell.has_top_wall:
            to_visit.append((i, j - 1))
        if j + 1 <= len(self._cells[0]) - 1 and not self._cells[i][j + 1].visited and not current_cell.has_bottom_wall:
            to_visit.append((i, j + 1))
    
        if len(to_visit) == 0:
            current_cell.draw()
            return
  
        for (chosen_i, chosen_j) in to_visit:
            current_cell.draw_move(self._cells[chosen_i][chosen_j])
            
            path_leads_to_exit = self._solve_r(chosen_i, chosen_j)
            if path_leads_to_exit:
                return True
            current_cell.draw_move(self._cells[chosen_i][chosen_j], undo=True)
        
        return False

            
          
        
        