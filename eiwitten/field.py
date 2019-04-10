class Field(object):
    """Initialises field for protein to fold in"""
    def __init__(self, length, sequence):
        self.dimension = (length * 2)
        self.field = [["_"] * self.dimension for i in range(self.dimension)]
        self.x_cdn = length
        self.y_cdn = length - 1

    """Fills field based on current option"""
    def fill_field(self, sequence, option):
        x = self.x_cdn
        y = self.y_cdn
        self.field[y][x - 1] = sequence[0]
        self.field[y][x] = sequence[1]
        for aminoacid, direction in zip(sequence[2:], option):
           if direction == "right":
               if self.field[y][x+1] == "_":
                   self.field[y][x+1] = aminoacid
                   x = x + 1
               else:
                   return False
           if direction == "up":
               if self.field[y-1][x] == "_":
                   self.field[y-1][x] = aminoacid
                   y = y - 1
               else:
                   return False
           if direction == "left":
               if self.field[y][x-1] == "_":
                   self.field[y][x-1] = aminoacid
                   x = x - 1
               else:
                   return False
           if direction == "down":
               if self.field[y+1][x] == "_":
                   self.field[y+1][x] = aminoacid
                   y = y + 1
               else:
                   return False
        return True

    def clear_field(self, length):
        for x in range(len(self.field)):
            for y in range(len(self.field)):
                self.field[y][x] = "_"
