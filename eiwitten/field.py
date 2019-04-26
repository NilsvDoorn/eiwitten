class Field(object):
    """Initialises field for protein to fold in"""
    def __init__(self, length, sequence):
        self.dimension = (length * 2)
        self.field = [["_"] * self.dimension for i in range(self.dimension)]
        self.x_cdn = length - 1
        self.y_cdn = length
        self.right_ways = {'[0, 1]': [1,0], '[0, -1]': [-1,0], '[1, 0]': [0,-1], '[-1, 0]': [0,1]}
        self.left_ways = {'[0, 1]': [-1,0], '[0, -1]': [1,0], '[1, 0]': [0,1], '[-1, 0]': [0,-1]}
        self.forward_ways = {'[0, 1]': [0,1], '[0, -1]': [0,-1], '[1, 0]': [1,0], '[-1, 0]': [-1,0]}
        self.coordinates = []

    """Fills field based on current option"""
    def fill_field(self, sequence, option):
        x = self.x_cdn
        y = self.y_cdn
        self.field[y-1][x] = sequence[0]
        self.field[y][x] = sequence[1]
        self.last_step = '[1, 0]'

        for aminoacid, direction in zip(sequence[2:], option):
           if direction == "right":
               new_direction = self.right_ways[self.last_step]
               if self.field[y + new_direction[0]][x + new_direction[1]] == "_":
                   y = y + new_direction[0]
                   x = x + new_direction[1]
                   self.field[y][x] = aminoacid
                   self.last_step = str(new_direction)
                   # trying out coordinates
                   self.coordinates.append((x, y))
               else:
                   return False
           elif direction == "forward":
               new_direction = self.forward_ways[self.last_step]
               if self.field[y + new_direction[0]][x + new_direction[1]] == "_":
                   y = y + new_direction[0]
                   x = x + new_direction[1]
                   self.field[y][x] = aminoacid
                   self.last_step = str(new_direction)
                   # trying out coordinates
                   self.coordinates.extend(self.field[x][y])
               else:
                   return False
           elif direction == "left":
               new_direction = self.left_ways[self.last_step]
               if self.field[y + new_direction[0]][x + new_direction[1]] == "_":
                   y = y + new_direction[0]
                   x = x + new_direction[1]
                   self.field[y][x] = aminoacid

                   self.last_step = str(new_direction)
                   # trying out coordinates
                   self.coordinates.extend(self.field[x][y])
               else:
                   return False
        return True

    def clear_field(self, length):
        for x in range(len(self.field)):
            for y in range(len(self.field)):
                self.field[y][x] = "_"
        # trying out coordinates
        self.coordinates = []
