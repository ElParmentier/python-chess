import tkinter as tk
from cell import *
from piece import *

root = tk.Tk()

class Board():
    def __init__(self):
        self.cells = {}

    def initBoard(self):
        columns = list(map(chr, range(97, 105))) # Generates list from a to h (inclusive)
        for i in range (0, 8):
            for j in columns:
                cell_coord = (columns.index(j), i)
                if i == 1 or i == 6:
                    self.cells[j + str(i + 1)] = Cell(Piece(cell_coord, "Pion"), cell_coord, tk.Label(root, width = 3))
                elif i == 0 or i == 7:
                    self.cells[j + str(i + 1)] = Cell(Piece(cell_coord, Piece.elites[columns.index(j)]), cell_coord, tk.Label(root, width = 3))
                else:
                    self.cells[j + str(i + 1)] = Cell(False, cell_coord, tk.Label(root, width = 3))
                created_cell = self.cells[j + str(i + 1)]
                created_cell.graphic_obj.config(bg = created_cell.bg_color, fg = created_cell.fg_color)
                created_cell.graphic_obj.grid(row = 8 - created_cell.coord[1], column = 8 - created_cell.coord[0])

    def displayBoardState(self):
        for cell in self.cells:
            print("La case {} {}".format(cell, self.cells[cell]))

    def displayPieceShortName(self, cell):
        if isinstance(current.occupied, Piece):
            return current_cell.occupied.piece_type[:1]

    def displayBoard(self):
        for current_cell in self.cells:
            cell = self.cells[current_cell]
            if isinstance(cell.occupied, Piece):
                cell.graphic_obj.config(text = 'A')



sampleMoves = ["e4 c5", "Nf3 Nc6", "d4 cxd4", "Nxd4 Nf6"]
board = Board()
board.initBoard()
board.displayBoard()

root.mainloop()
