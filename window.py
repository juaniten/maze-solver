from tkinter import Tk, BOTH, Canvas

class window():
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
        self.__root = Tk()
        self.__root.title = "Maze solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root)
        self.__canvas.pack()
        self.__window_running = False
        

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()

    def close(self):
        self.__window_running = False

    