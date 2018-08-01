class Cell():
    def __init__(self, occupied, coord, graphic_obj):
        self.occupied = occupied
        self.coord = coord
        self.graphic_obj = graphic_obj
        self.color = "noire" if (coord[0] + coord[1]) % 2 == 0 else "blanche"

    def __str__(self):
        if (self.occupied == False):
            return "{} position {} est {}".format(self.color, self.coord, "vide")
        return "{} position {} est occupée par un {}".format(self.color, self.coord, self.occupied.piece_type)
