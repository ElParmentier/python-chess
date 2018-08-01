class Cell():
    def __init__(self, occupied, coord, graphic_obj):
        self.occupied = occupied
        self.coord = coord
        self.graphic_obj = graphic_obj

    def __str__(self):
        if (self.occupied == False):
            return "position {} est {}".format(self.coord, "vide")
        return "position {} est occupée par un {}".format(self.coord, self.occupied.piece_type)
