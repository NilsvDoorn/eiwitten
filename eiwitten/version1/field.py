class Field(object):
    """Initialises field for protein to fold in"""
    def __init__(self, length):
        self.dimension = length
        self.field = [["_"] * self.dimension for i in range(self.dimension)]

    """Fills field based on current option"""
    def fill_field(self, sequence, option):
        for aminoacid, position in zip(sequence, option):
            self.field[position[0]][position[1]] = aminoacid
        return True

    def clear_field(self, length):
        for x in range(len(self.field)):
            for y in range(len(self.field)):
                self.field[y][x] = "_"
