from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)
    
    p1 = Point(10, 10)
    p2 = Point(20, 20)
    p3 = Point (0, 40)
    p4 = Point(40, 60)

    cell1 = Cell(p1, p2, win)
    cell1.has_bottom_wall = False
    cell2 = Cell(p3, p4, win)

    cell1.draw()
    cell2.draw()
    
    win.wait_for_close()



if __name__ == '__main__':
    main()