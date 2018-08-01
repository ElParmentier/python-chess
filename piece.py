class Piece():
    not_pawn = ["Tour", "Cavalier", "Fou", "Reine", "Roi", "Fou", "Cavalier", "Tour"]
    def __init__(self, coord, piece_type):
        self.coord = coord
        self.piece_type = piece_type
