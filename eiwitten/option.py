from itertools import product
from math import ceil
"""Generates a list of all folding options for the protein"""
class Option(object):
    def __init__(self):
        self.options = ["right", "forward", "left", "up", "down"]

    def mirror(self, route):
        for option in route:
            if option == 'right':
                return False
            elif option == 'left' or option == "up" or option == "down":
                return True
        return True

    """Fills field based on current option"""
    def amino_positions(self, sequence, option):
        # initialises positions list and starting coordinates of protein
        positions = []
        begin = int(ceil(len(sequence) / 2))

        # appends first two positions to positions list
        positions.append(tuple((begin, begin, begin)))
        positions.append(tuple((begin, begin + 1, begin)))

        # initialises x-, y-coordinates and current direction
        x, y, z = begin, begin + 1, begin
        directions = {'y_min':{'right': [1,0,0,'x_min'], 'left': [-1,0,'x_plus'], 'forward': [0,-1]},
                    'x_plus':{'right': [0,-1,0,'y_min'], 'left': [0,1,0,'y_plus'], 'up': [0,0,1,'z_plus'], 'down': [0,0,-1,'z_min'], 'forward': [1,0,0,'x_plus']},
                    'x_min':{'right': [0,1,'y_plus'], 'left': [0,-1,'y_min'], 'forward': [1,0]},
                    'y_plus':{'right': [-1,0,'x_plus'], 'left': [1,0,'x_min'], 'forward': [0,1]},
                    'z_plus':{'right': [-1,0,'x_plus'], 'left': [1,0,'x_min'], 'forward': [0,1]},
                    'z_min':{'right': [-1,0,'x_plus'], 'left': [1,0,'x_min'], 'forward': [0,1]}}
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
