import tkinter as tk
from cell import *
from piece import *

class Board():
    def __init__(self):
        self.cells = {}

    def generateBoard(self):
        columns = list(map(chr, range(97, 105))) # Generates list from a to h (inclusive)
        for i in range (0, 8):
            for j in columns:
                cell_coord = (columns.index(j), i)
                if i == 1 or i == 6:
                    self.cells[j + str(i + 1)] = Cell(Piece(cell_coord, "Pion"), cell_coord, False)
                elif i == 0 or i == 7:
                    self.cells[j + str(i + 1)] = Cell(Piece(cell_coord, Piece.not_pawn[columns.index(j)]), cell_coord, False)
                else:
                    self.cells[j + str(i + 1)] = Cell(False, cell_coord, False)

    def displayBoardState(self):
        for cell in self.cells:
            print("La case {} {}".format(cell, self.cells[cell]))

sampleMoves = ["e4 	c5", "Nf3 	Nc6", "d4 	cxd4", "Nxd4 	Nf6"]
board = Board()
board.generateBoard()
board.displayBoardState()
