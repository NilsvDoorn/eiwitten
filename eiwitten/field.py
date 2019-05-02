class Field(object):
    """Initialises field for protein to fold in"""
    def __init__(self, length, sequence):
        self.dimension = (length * 2)
        self.field = [["_"] * self.dimension for i in range(self.dimension)]

    """Fills field based on current option"""
    def fill_field(self, positions, sequence):
        for position, aminoacid in zip(positions, sequence):
            (x, y) = position
            self.field[x][y] = aminoacid
