from itertools import product
from math import ceil
"""Generates a list of all folding options for the protein"""
class Option(object):
    def __init__(self):
        self.options = ["right", "forward", "left", "up", "down","back"]
        self.options_2D = ["right", "forward", "left"]

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

        # initialises x-, y- and z-coordinates and current direction
        x, y, z = begin, begin + 1, begin
        # directions = {'y_min':{'1':{'right': [-1,0,0,'x_min','1'], 'left': [1,0,0,'x_plus','1'], 'forward': [0,1,0,'y_min','1'], 'up':[0,0,1,'z_plus','1'], 'down': [0,0,-1,'z_min']},
        #                         '2':{'right': [1,0,0,'x_plus','2'], 'left': [-1,0,0,'x_min','2'], 'forward': [0,1,0,'y_min','2'], 'up':[0,0,-1,'z_min'], 'down': [0,0,1,'z_plus']},
        #                         '3':{'right': [0,0,-1,'z_min','3'], 'left': [0,0,1,'z_plus','3'], 'forward': [0,1,0,'y_min','3'], 'up':[1,0,0,'x_plus'], 'down': [-1,0,0,'x_min']},
        #                         '4':{'right': [0,0,1,'z_plus','4'], 'left': [0,0,-1,'z_min','4'], 'forward': [0,1,0,'y_min','4'], 'up':[-1,0,0,'x_min'], 'down': [1,0,0,'x_plus']}},
        #             'x_plus':{'1':{'right': [0,1,'y_min','1'], 'left': [0,-1,'y_plus','1'], 'forward': [1,0,'x_plus','1'], 'up':[0,0,1,'z_plus'], 'down': [0,0,-1,'z_min']},
        #
        #             'x_min':{'1':{'right': [0,-1,'y_plus'], 'left': [0,1,'y_min'], 'forward': [-1,0,'x_min'], 'up':[0,0,1,'z_plus'], 'down': [0,0,-1,'z_min']},
        #             'y_plus':{'1':{'right': [1,0,'x_plus'], 'left': [-1,0,'x_min'], 'forward': [0,-1,'y_plus'], 'up':[0,0,1,'z_plus'], 'down': [0,0,-1,'z_min']},
        #             'z_plus':{'1':{'right': [-1,0,'x_plus'], 'left': [1,0,'x_min'], 'forward': [0,1]},
        #             'z_min':{'1':{'right': [-1,0,'x_plus'], 'left': [1,0,'x_min'], 'forward': [0,1]}}
        direction = 'forward'
        going_back = {'left':'right','right':'left','forward':'back','back':'forward','up':'down','down':'up'}
        new_directions = {'left':[-1,0,0],'right':[1,0,0],'forward':[0,1,0],'back':[0,-1,0],'up':[0,0,1],'down':[0,0,-1],}
        # loops over current option and appends aminoacid coordinates
        # if there are no bumps
        for move in option:
            # x += directions[direction[0]][direction[1]][move][0]
            # y += directions[direction[0]][direction[1]][move][1]
            # z += directions[direction[0]][direction[1]][move][2]
            # helper = direction[0]
            # direction[0] = directions[direction[0]][direction[1]][move][3]
            # direction[1] = directions[helper][direction[1]][move][4]
            if not going_back[move] == direction:
                x += new_directions[move][0]
                y += new_directions[move][1]
                z += new_directions[move][2]
                direction = move

            # if direction == "x_plus":
            #     if move == "right":
            #         y = y - 1
            #         direction = "y_min"
            #     elif move == "left":
            #         y = y + 1
            #         direction = "y_plus"
            #     elif move == "up":
            #         z = z + 1
            #         direction = "z_plus"
            #     elif move == "down":
            #         z = z - 1
            #         direction = "z_min"
            #     elif move == "forward":
            #         x = x + 1
            # elif direction == "y_min":
            #     if move == "right":
            #         x = x + 1
            #         direction = "x_plus"
            #     elif move == "left":
            #         x = x - 1
            #         direction = "x_min"
            #     elif move == "up":
            #         z = z + 1
            #         direction = "z_plus"
            #     elif move == "down":
            #         z = z - 1
            #         direction = "z_min"
            #     elif move == "forward":
            #         y = y + 1
            # elif direction == "y_plus":
            #     if move == "right":
            #         x = x - 1
            #         direction = "x_min"
            #     elif move == "left":
            #         x = x + 1
            #         direction = "x_plus"
            #     elif move == "up":
            #         z = z + 1
            #         direction = "z_plus"
            #     elif move == "down":
            #         z = z - 1
            #         direction = "z_min"
            #     elif move == "forward":
            #         y = y - 1
            # elif direction == "x_min":
            #     if move == "right":
            #         y = y + 1
            #         direction = "y_plus"
            #     elif move == "left":
            #         y = y - 1
            #         direction = "y_min"
            #     elif move == "up":
            #         z = z + 1
            #         direction = "z_plus"
            #     elif move == "down":
            #         z = z - 1
            #         direction = "z_min"
            #     elif move == "forward":
            #         x = x - 1
            # elif direction == "z_plus":
            #     if move == "right":
            #         x = x + 1
            #         direction = "x_plus"
            #     elif move == "left":
            #         x = x - 1
            #         direction = "x_min"
            #     elif move == "up":
            #         y = y + 1
            #         direction = "y_plus"
            #     elif move == "down":
            #         y = y - 1
            #         direction = "y_min"
            #     elif move == "forward":
            #         z = z + 1
            # elif direction == "z_min":
            #     if move == "right":
            #         x = x + 1
            #         direction = "x_plus"
            #     elif move == "left":
            #         x = x - 1
            #         direction = "x_min"
            #     elif move == "up":
            #         y = y + 1
            #         direction = "y_plus"
            #     elif move == "down":
            #         y = y - 1
            #         direction = "y_min"
            #     elif move == "forward":
            #         z = z - 1
            # only appends coordinates if there are no bumps
            if tuple((x, y, z)) in positions:
                return False
            positions.append(tuple((x, y, z)))
        return positions
