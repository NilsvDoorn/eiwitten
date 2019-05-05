from itertools import product
from math import ceil
"""Generates a list of all folding options for the protein"""
class Option(object):
    def __init__(self, length):
        self.options = ["right", "forward", "left"]

    def mirror(self, route):
        for option in route:
            if option == 'right':
                return False
            elif option == 'left':
                return True
        return True

    """Fills field based on current option"""
    def amino_positions(self, sequence, option):
        # initialises positions list and starting coordinates of protein
        positions = []
        begin = int(ceil(len(sequence) / 2))

        # appends first two positions to positions list
        positions.append(tuple((begin, begin)))
        positions.append(tuple((begin + 1, begin)))

        # initialises x-, y-coordinates and current direction
        x, y = begin, begin + 1
        direction = "d"

        # loops over current option and appends aminoacid coordinates
        # if there are no bumps
        for move in option:
            if direction == "d":
                if move == "right":
                    x = x - 1
                    direction = "l"
                elif move == "left":
                    x = x + 1
                    direction = "r"
                elif move == "forward":
                    y = y + 1
            elif direction == "r":
                if move == "right":
                    y = y + 1
                    direction = "d"
                elif move == "left":
                    y = y - 1
                    direction = "u"
                elif move == "forward":
                    x = x + 1
            elif direction == "l":
                if move == "right":
                    y = y - 1
                    direction = "u"
                elif move == "left":
                    y = y + 1
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
                    y = y - 1
            # only appends coordinates if there are no bumps
            if tuple((y, x)) in positions:
                return False
            positions.append(tuple((y, x)))
        return positions
