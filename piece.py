from enum import Enum

class PieceType(Enum):
    Pawn = 0
    Rook = 1
    Knight = 2
    Bishop = 3
    Queen = 4
    King = 5

class Piece():
    pieces = {
        "Pawn": PieceType.Pawn,
        "Rook": PieceType.Rook,
        "Knight": PieceType.Knight,
        "Bishop": PieceType.Bishop,
        "Queen": PieceType.Queen,
        "King": PieceType.King
    }
    def __init__(self, coord, piece_type):
        self.coord = coord
        self.piece_type = self.pieces[piece_type]
    def __str__(self):
        return "{} en {}".format(self.piece_type.name, self.coord)
