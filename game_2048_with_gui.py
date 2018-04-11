from tkinter import *
from game_2048_no_gui import *

SIZE = 500
GRID_LEN = 4
GRID_PADDING = 10
FONT = ("Verdana", 40, "bold")
BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = { 2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
                          32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
                          512:"#edc850", 1024:"#edc53f", 2048:"#edc22e" }
CELL_COLOR_DICT = { 2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", \
                    32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", \
                    512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2" }


class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.operation)

        self.matrix = init()
        self.matrix_stack = []
        self.grid_matrix = []

        self.createWidgets()
        self.updateWidgets()

        self.mainloop()


    def createWidgets(self):
        background = Frame(self, bg=BACKGROUND_COLOR_GAME, width=SIZE, height=SIZE)
        background.grid()
        for i in range(GRID_LEN):
            grid_row = []
            for j in range(GRID_LEN):
                cell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY, width=SIZE / GRID_LEN, height=SIZE / GRID_LEN)
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=4, height=2)
                t.grid()
                grid_row.append(t)
            self.grid_matrix.append(grid_row)


    def updateWidgets(self):
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                num = self.matrix[i*4 + j]
                if num != 0:
                    self.grid_matrix[i][j].configure(text=num, bg=BACKGROUND_COLOR_DICT[num])
                else:
                    self.grid_matrix[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
        self.update_idletasks()


    def operation(self, event):
        self.matrix_stack.append(list(self.matrix))
        key = repr(event.char)
        if key == "'w'":
            self.matrix = move(self.matrix, "w")
        elif key == "'a'":
            self.matrix = move(self.matrix, "a")
        elif key == "'s'":
            self.matrix = move(self.matrix, "s")
        elif key == "'d'":
            self.matrix = move(self.matrix, "d")
        elif key == "'q'":
            exit()
        if not isSame(self.matrix_stack[-1], self.matrix):
            self.matrix = add(self.matrix)
        self.updateWidgets()
        if isWin(self.matrix):
            self.grid_matrix[1][1].configure(text="You", bg=BACKGROUND_COLOR_CELL_EMPTY)
            self.grid_matrix[1][2].configure(text="Win!", bg=BACKGROUND_COLOR_CELL_EMPTY)
        if isOver(self.matrix):
            self.grid_matrix[1][1].configure(text="You", bg=BACKGROUND_COLOR_CELL_EMPTY)
            self.grid_matrix[1][2].configure(text="Lose!", bg=BACKGROUND_COLOR_CELL_EMPTY)


if __name__ == '__main__':
    game = Game2048()

