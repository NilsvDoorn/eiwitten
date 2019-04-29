from itertools import product
from math import ceil
"""Generates a list of all folding options for the protein"""
class Option(object):
    def __init__(self, length):
        self.options = ["right", "left", "forward"]

    """Fills field based on current option"""
    def amino_positions(self, sequence, option):
        positions = []
        begin = ceil(len(sequence) / 2)
        positions.append(tuple((begin, begin)))
        positions.append(tuple((begin + 1, begin)))
        x, y = begin, begin + 1
        direction = "d"
        for aminoacid, move in zip(sequence[2:], option):
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
            if tuple((y, x)) in positions:
                return False
            positions.append(tuple((y, x)))
        return positions
