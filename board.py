import tkinter as tk
from cell import *

class Board():
    def __init__(self):
        self.cells = {}

    def generateBoard(self):
        columns = list(map(chr, range(97, 105))) # Generates list from a to h (inclusive)
        for i in range (0, 8):
            for j in columns:
                self.cells[j + str(i + 1)] = Cell(False, (columns.index(j), i), False)

    def displayBoardState(self):
        for cell in self.cells:
            print("La case {} {}".format(cell, self.cells[cell]))

board = Board()
board.generateBoard()
board.displayBoardState()
