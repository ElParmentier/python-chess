import tkinter as tk
from cell import *
from piece import *

root = tk.Tk()

class Board():
    def __init__(self):
        self.cells = {}
        self.elites = []
        for i in range(1, 6):
            self.elites.append(PieceType(i).name)
        for i in reversed(range(1, 4)):
            self.elites.append(PieceType(i).name)

    def initBoard(self):
        columns = list(map(chr, range(97, 105))) # Generates list from a to h (inclusive)
        for i in range (0, 8):
            for j in columns:
                cell_coord = (columns.index(j), i)
                if i == 1 or i == 6:
                    self.cells[j + str(i + 1)] = Cell(Piece(cell_coord, "Pawn"), cell_coord, tk.Label(root, width = 5, height = 2))
                elif i == 0 or i == 7:
                    self.cells[j + str(i + 1)] = Cell(Piece(cell_coord, self.elites[columns.index(j)]), cell_coord, tk.Label(root, width = 5, height = 2))
                else:
                    self.cells[j + str(i + 1)] = Cell(False, cell_coord, tk.Label(root, width = 5, height = 2))
                created_cell = self.cells[j + str(i + 1)]
                created_cell.graphic_obj.config(bg = created_cell.bg_color, fg = created_cell.fg_color)
                created_cell.graphic_obj.grid(row = 8 - created_cell.coord[1], column = created_cell.coord[0])

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
                cell.graphic_obj.config(text = cell.occupied.piece_type.name[:1])



sampleMoves = ["e4 c5", "Nf3 Nc6", "d4 cxd4", "Nxd4 Nf6"]
board = Board()
board.initBoard()
board.displayBoard()

root.mainloop()
