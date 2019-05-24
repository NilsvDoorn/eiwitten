import random
from math import ceil
from copy import deepcopy
from itertools import product

"""Generates a random option of the sequence *args of length repeat"""
def random_product(*args, repeat):

    # Random selection from itertools.product(*args, **kwds)
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(random.choice(pool) for pool in pools)


"""Generates random option until one is found that contains no bumps (2D)"""
def viable_random_product_2d(length):

    best_fold = list(random_product(["right", "left", "forward"], repeat = length))
    while not amino_positions_2d(best_fold, True):
        best_fold = list(random_product(["right", "left", "forward"], repeat = length))
    return best_fold


"""Generates a list of all possible fold options of length length (2D)"""
def all_options_2d(length):
    return list(product(["forward", "left", "right"], repeat = length))


"""Funcion for avoiding mirrored folds"""
def mirror(route):
    for option in route:
        if option == 'right':
            return False
        elif option == 'left' or option == "up" or option == "down":
            return True
    return True


"""Finds aminoacid positions in current fold and checks for bumps (2D)"""
def amino_positions_2d(option, hillclimber):

    # initialises positions list and starting coordinates of protein
    positions = []
    begin = ceil(len(option) // 2)

    if not hillclimber:
        # appends first two positions to positions list
        positions.append(tuple((begin, begin)))
        positions.append(tuple((begin + 1, begin)))

    # initialises x-, y-coordinates and current direction
    x, y = begin, begin + 1

    # right, left and forward change with last direction
    directions = {'y_min':{'right': [-1,0,'x_min'], 'left': [1,0,'x_plus'], 'forward': [0,1,'y_min']},
                'x_plus':{'right': [0,1,'y_min'], 'left': [0,-1,'y_plus'], 'forward': [1,0,'x_plus']},
                'x_min':{'right': [0,-1,'y_plus'], 'left': [0,1,'y_min'], 'forward': [-1,0,'x_min']},
                'y_plus':{'right': [1,0,'x_plus'], 'left': [-1,0,'x_min'], 'forward': [0,-1,'y_plus']}}
    direction = "y_min"

    # loops over current option and appends aminoacid coordinates
    # if there are no bumps
    for move in option:
        x += directions[direction][move][0]
        y += directions[direction][move][1]
        direction = directions[direction][move][2]

        # only appends coordinates if there are no bumps
        if tuple((y, x)) in positions:
            return False
        positions.append(tuple((y, x)))
    return positions

"""Checks the points scored by the current fold (2D, non-Hillclimber)"""
def fold_points_2d(positions, sequence):

    points = 0
    HHHH = []
    CCCC = []
    for position, acid in zip(positions, sequence):
        if acid == "H":
            HHHH.append(position)
        elif acid == "C":
            CCCC.append(position)
    print(HHHH)
    print(CCCC)
    for acid_position in HHHH:
        for look_around in [[1,0],[-1,0],[0,1],[0,-1]]:
            if (acid_position[0] + look_around[0], acid_position[1] + look_around[1]) in HHHH:
                points += 1

    for acid_position in CCCC:
        for look_around in [[1,0],[-1,0],[0,1],[0,-1]]:
            if (acid_position[0] + look_around[0], acid_position[1] + look_around[1]) in CCCC:
                points += 5
            elif (acid_position[0] + look_around[0], acid_position[1] + look_around[1]) in HHHH:
                points += 2
    return points / 2
