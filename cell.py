class Cell():
    def __init__(self, occupied, coord, graphic_obj):
        self.occupied = occupied
        self.coord = coord
        self.graphic_obj = graphic_obj

    def __str__(self):
        return "position {} est {}".format(self.coord, "occupée" if self.occupied else "vide")
