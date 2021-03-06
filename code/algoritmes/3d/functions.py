import random
from math import ceil
from copy import deepcopy
from itertools import product

"""Generates a random option of the sequence *args of length repeat"""
def random_product(*args, repeat):

    # Random selection from itertools.product(*args, **kwds)
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(random.choice(pool) for pool in pools)


"""Generates random option until one is found that contains no bumps (3D)"""
def viable_random_product_3d(length):

    best_fold = list(random_product(["forward", "right", "left", "up", "down", "back"], repeat = length))
    while not amino_positions_3d(best_fold, True):
        best_fold = list(random_product(["forward", "right", "left", "up", "down", "back"], repeat = length))
    return best_fold

"""Generates a list of all possible fold options of length length (3D)"""
def all_options_3d(length):
    return list(product(["forward", "left", "right", "up", "down", "back"], repeat = length))


"""Funcion for avoiding mirrored folds"""
def mirror(route):
    for option in route:
        if option == 'right':
            return False
        elif option == 'left' or option == "up" or option == "down" or option == "back":
            return True
    return True


"""Finds aminoacid positions in current fold and checks for bumps (3D)"""
def amino_positions_3d(option, hillclimber):

    # initialises positions list and starting coordinates of protein
    positions = []
    begin = int(ceil(len(option) / 2))

    # if hillclimber is True, hillclimber first two positions aren't constant
    if not hillclimber:
        # appends first two positions to positions list
        positions.append(tuple((begin, begin, begin)))
        positions.append(tuple((begin, begin + 1, begin)))

    # initialises x-, y- and z-coordinates and current direction
    x, y, z = begin, begin + 1, begin

    # right, left and forward change with last direction
    direction = 'forward'
    going_back = {'left':'right','right':'left','forward':'back','back':'forward','up':'down','down':'up'}
    new_directions = {'left':[-1,0,0],'right':[1,0,0],'forward':[0,1,0],'back':[0,-1,0],'up':[0,0,1],'down':[0,0,-1],}

    # loops over current option and appends aminoacid coordinates
    for move in option:
        if not going_back[move] == direction:
            x += new_directions[move][0]
            y += new_directions[move][1]
            z += new_directions[move][2]
            direction = move

        # only appends coordinates if there are no bumps
        if tuple((x, y, z)) in positions:
            return False
        positions.append(tuple((x, y, z)))
    return positions

"""Checks the points scored by the current fold (3D)"""
def fold_points_3d(positions, sequence):

    # initialises lists for positions of H's and C's and points
    points = 0
    HHHH = []
    CCCC = []

    # finds all H- and C-positions
    for position, acid in zip(positions, sequence):
        if acid == "H":
            HHHH.append(position)
        elif acid == "C":
            CCCC.append(position)

    # checks for H-H connections
    for acid_position in HHHH:
        for direction in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
            if (acid_position[0] + direction[0], acid_position[1] + direction[1], acid_position[2] + direction[2]) in HHHH:
                points += 1

    # checks for H-C and C-C connections
    for acid_position in CCCC:
        for direction in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
            if (acid_position[0] + direction[0], acid_position[1] + direction[1], acid_position[2] + direction[2]) in CCCC:
                points += 5
            elif (acid_position[0] + direction[0], acid_position[1] + direction[1], acid_position[2] + direction[2]) in HHHH:
                points += 2
    return points / 2
