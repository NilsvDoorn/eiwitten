from itertools import product
import random
"""Generates a list of all folding options for the protein"""
class Option(object):
    def __init__(self, length):
#        self.options = list(product(["right", "left", "forward"], repeat = length - 2))
        self.option = list(random_product(["right", "left", "forward", "up", "down"], repeat = length))
        self.positions = amino_positions(list(self.option), length)
        while not self.positions:
            self.option = list(random_product(["right", "left", "forward",  "up", "down"], repeat = length))
            self.positions = amino_positions(list(self.option), length)

# from https://docs.python.org/3.1/library/itertools.html?highlight=combinations#itertools.product
# generates a random sequence of left, forward and right of length protein.length
def random_product(*args, repeat):
    "Random selection from itertools.product(*args, **kwds)"
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(random.choice(pool) for pool in pools)

# finds all x,y amino positions of current option
def amino_positions(option, length):
    # initialises positions list and starting coordinates of protein
    positions = []
    begin = int((length / 2))

    # appends first two positions to positions list
    positions.append(tuple((begin, begin, begin)))
    positions.append(tuple((begin, begin + 1, begin)))

    # initialises x-, y-coordinates and current direction
    x, y, z = begin, begin + 1, begin
    direction = "x_min"

    # loops over current option and appends aminoacid coordinates
    # if there are no bumps
    for move in option:
        if direction == "x_plus":
            if move == "right":
                y = y - 1
                direction = "y_min"
            elif move == "left":
                y = y + 1
                direction = "y_plus"
            elif move == "up":
                z = z + 1
                direction = "z_plus"
            elif move == "down":
                z = z - 1
                direction = "z_min"
            elif move == "forward":
                x = x + 1
        elif direction == "y_plus":
            if move == "right":
                x = x + 1
                direction = "x_plus"
            elif move == "left":
                x = x - 1
                direction = "x_min"
            elif move == "up":
                z = z + 1
                direction = "z_plus"
            elif move == "down":
                z = z - 1
                direction = "z_min"
            elif move == "forward":
                y = y + 1
        elif direction == "y_min":
            if move == "right":
                x = x - 1
                direction = "x_min"
            elif move == "left":
                x = x + 1
                direction = "x_plus"
            elif move == "up":
                z = z + 1
                direction = "z_plus"
            elif move == "down":
                z = z - 1
                direction = "z_min"
            elif move == "forward":
                y = y - 1
        elif direction == "x_min":
            if move == "right":
                y = y + 1
                direction = "y_plus"
            elif move == "left":
                y = y - 1
                direction = "y_min"
            elif move == "up":
                z = z + 1
                direction = "z_plus"
            elif move == "down":
                z = z - 1
                direction = "z_min"
            elif move == "forward":
                x = x - 1
        elif direction == "z_plus":
            if move == "right":
                x = x + 1
                direction = "x_plus"
            elif move == "left":
                x = x - 1
                direction = "x_min"
            elif move == "up":
                y = y + 1
                direction = "y_plus"
            elif move == "down":
                y = y - 1
                direction = "y_min"
            elif move == "forward":
                z = z + 1
        elif direction == "z_min":
            if move == "right":
                x = x + 1
                direction = "x_plus"
            elif move == "left":
                x = x - 1
                direction = "x_min"
            elif move == "up":
                y = y + 1
                direction = "y_plus"
            elif move == "down":
                y = y - 1
                direction = "y_min"
            elif move == "forward":
                z = z - 1
        # only appends coordinates if there are no bumps
        if tuple((x, y, z)) in positions:
            return False
        positions.append(tuple((x, y, z)))
    return positions

# determines if current fold option results in bumps
def viable_option(option):
    number = 1
    for position in option:
        for i in range(len(option) - number):
            if option[i + number] == position:
                return False
        number = number + 1
    return True

    # def automatic(self, option, protein):
    #     for i in range(len(protein)):
    #         if protein[i] == protein[i+4] == "H":
    #             if option[i] == option[i+1] == "left" or option[i] == option[i+1] == "right":
    #                 return False
    #                 self.count += 1
    #                 print(self.count)
    #                 i += 4
    #     return True
