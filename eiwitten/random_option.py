from itertools import product
import random
"""Generates a list of all folding options for the protein"""
class Option(object):
    def __init__(self, length):
#        self.options = list(product(["right", "left", "forward"], repeat = length - 2))
        self.option = random_product(["right", "left", "forward"], repeat = length)
        self.positions = amino_positions(list(self.option))
        while not viable_option(self.positions):
            self.option = random_product(["right", "left", "forward"], repeat = length)
            self.positions = amino_positions(list(self.option))

# from https://docs.python.org/3.1/library/itertools.html?highlight=combinations#itertools.product
# generates a random sequence of left, forward and right of length protein.length
def random_product(*args, repeat):
    "Random selection from itertools.product(*args, **kwds)"
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(random.choice(pool) for pool in pools)

# finds all x,y amino positions of current option
def amino_positions(option):
    positions = []
    x, y = 0, 0
    positions.append(tuple((x, y + 1)))
    positions.append(tuple((x, y)))
    direction = "d"
    for move in option:
        if direction == "d":
            if move == "right":
                x = x - 1
                direction = "l"
            elif move == "left":
                x = x + 1
                direction = "r"
            elif move == "forward":
                y = y - 1
        elif direction == "r":
            if move == "right":
                y = y - 1
                direction = "d"
            elif move == "left":
                y = y + 1
                direction = "u"
            elif move == "forward":
                x = x + 1
        elif direction == "l":
            if move == "right":
                y = y + 1
                direction = "u"
            elif move == "left":
                y = y - 1
                direction = "d"
            elif move == "forward":
                x = x - 1
        elif direction == "u":
            if move == "right":
                x = x + 1
                direction = "r"
            elif move == "left":
                x = x - 1
                direction = "l"
            elif move == "forward":
                y = y + 1
        positions.append(tuple((x, y)))
    return positions

# determines if current fold option results in bumps
def viable_option(option):
    number = 1
    for position in option:
        for i in range(len(option) - number):
            if option[i + number] == position:
                print("Bump:")
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
