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
    while not amino_positions_2d_hc(best_fold):
        best_fold = list(random_product(["right", "left", "forward"], repeat = length))
    return best_fold


"""Generates random option until one is found that contains no bumps (3D)"""
def viable_random_product_3d(length):

    best_fold = list(random_product(["right", "left", "forward", "up", "down"], repeat = length))
    while not amino_positions_3d_hc(best_fold):
        best_fold = list(random_product(["right", "left", "forward", "up", "down"], repeat = length))
    return best_fold


"""Generates a list of all possible fold options of length length (2D)"""
def all_options_2d(length):
    return list(product(["forward", "left", "right"], repeat = length))


"""Generates a list of all possible fold options of length length (3D)"""
def all_options_3d(length):
    return list(product(["forward", "left", "right", "up", "down"], repeat = length))


"""Funcion for avoiding mirrored folds"""
def mirror(route):
    for option in route:
        if option == 'right':
            return False
        elif option == 'left' or option == "up" or option == "down":
            return True
    return True


"""Finds aminoacid positions in current fold and checks for bumps (2D, non-Hillclimber)"""
def amino_positions_2d(option):

    # initialises positions list and starting coordinates of protein
    positions = []
    begin = ceil(len(option) // 2)

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


"""Finds aminoacid positions in current fold and checks for bumps (2D, Hillclimber)"""
def amino_positions_2d_hc(option):

    # initialises positions list and starting coordinates of protein
    positions = []
    begin = ceil(len(option) // 2)

    # initialises x-, y-coordinates and current direction
    x, y = begin, begin + 1

    # right, left and forward change with last direction
    directions = {'y_min':{'right': [-1,0,'x_min'], 'left': [1,0,'x_plus'], 'forward': [0,1,'y_min']},
                'x_plus':{'right': [0,1,'y_min'], 'left': [0,-1,'y_plus'], 'forward': [1,0,'x_plus']},
                'x_min':{'right': [0,-1,'y_plus'], 'left': [0,1,'y_min'], 'forward': [-1,0,'x_min']},
                'y_plus':{'right': [1,0,'x_plus'], 'left': [-1,0,'x_min'], 'forward': [0,-1,'y_plus']}}
    direction = "y_min"

    # loops over current option and finds aminoacid coordinates
    for move in option:
        x += directions[direction][move][0]
        y += directions[direction][move][1]
        direction = directions[direction][move][2]

        # only appends coordinates if there are no bumps
        if tuple((y, x)) in positions:
            return False
        positions.append(tuple((y, x)))
    return positions


"""Finds aminoacid positions in current fold and checks for bumps (3D, non-Hillclimber)"""
def amino_positions_3d(option):

    # initialises positions list and starting coordinates of protein
    positions = []
    begin = int(ceil(len(option) / 2))

    # appends first two positions to positions list
    positions.append(tuple((begin, begin, begin)))
    positions.append(tuple((begin, begin + 1, begin)))

    # initialises x-, y- and z-coordinates and current direction
    x, y, z = begin, begin + 1, begin

    direction = 'forward'
    going_back = {'left':'right','right':'left','forward':'back','back':'forward','up':'down','down':'up'}
    new_directions = {'left':[-1,0,0],'right':[1,0,0],'forward':[0,1,0],'back':[0,-1,0],'up':[0,0,1],'down':[0,0,-1],}

    for move in option:
        if not going_back[move] == direction:
            x += new_directions[move][0]
            y += new_directions[move][1]
            z += new_directions[move][2]
            direction = move

        if tuple((x, y, z)) in positions:
            return False
        positions.append(tuple((x, y, z)))
    return positions


"""Finds aminoacid positions in current fold and checks for bumps (3D, Hillclimber)"""
def amino_positions_3d_hc(option):

    # initialises positions list and starting coordinates of protein
    positions = []
    begin = int(ceil(len(option) / 2))

    # initialises x-, y-coordinates and current direction
    x, y, z = begin, begin + 1, begin

    direction = 'forward'
    going_back = {'left':'right','right':'left','forward':'back','back':'forward','up':'down','down':'up'}
    new_directions = {'left':[-1,0,0],'right':[1,0,0],'forward':[0,1,0],'back':[0,-1,0],'up':[0,0,1],'down':[0,0,-1],}

    for move in option:
        if not going_back[len(option) - 1] == direction:
            x += new_directions[move][0]
            y += new_directions[move][1]
            z += new_directions[move][2]
            direction = move

        # only appends coordinates if there are no bumps
        if tuple((x, y, z)) in positions:
            return False
        positions.append(tuple((x, y, z)))

    # returns a list of all the current fold's aminoacids' positions
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


"""checks the points scored by the current fold (2D, Hillclimber)"""
def fold_points_2d_hc(positions, protein):

    # initialises list of points, H-positions and C-positions
    points = 0
    HHHH = []
    CCCC = []

    # finds positions of all H's and C's
    for position, acid in zip(positions, protein.sequence):
        if acid == "H":
            HHHH.append(position)
        elif acid == "C":
            CCCC.append(position)

    # finds all H-H connections
    for acid_position in HHHH:
        for look_around in [[1,0],[-1,0],[0,1],[0,-1]]:
            if (acid_position[0] + look_around[0], acid_position[1] + look_around[1]) in HHHH:
                points += 1

    # finds all H-C and C-C connections
    for acid_position in CCCC:
        for look_around in [[1,0],[-1,0],[0,1],[0,-1]]:
            if (acid_position[0] + look_around[0], acid_position[1] + look_around[1]) in CCCC:
                points += 5
            elif (acid_position[0] + look_around[0], acid_position[1] + look_around[1]) in HHHH:
                points += 2

    # returns points scored by current fold
    return (points / 2)  - protein.errorpoint[-1]


"""Checks the points scored by the current fold (3D, non-Hillclimber)"""
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
        for look_around in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
            if (acid_position[0] + look_around[0], acid_position[1] + look_around[1], acid_position[2] + look_around[2]) in CCCC:
                points += 5
            elif (acid_position[0] + look_around[0], acid_position[1] + look_around[1], acid_position[2] + look_around[2]) in HHHH:
                points += 2
    return points / 2


"""checks the points scored by the current fold (3D, Hillclimber)"""
def fold_points_3d_hc(positions, protein):

    # initialises lists for positions of H's and C's and points
    points = 0
    HHHH = []
    CCCC = []

    # finds all H and C positions
    for position, acid in zip(positions, protein.sequence):
        if acid == "H":
            HHHH.append(position)
        elif acid == "C":
            CCCC.append(position)

    # finds all H-H connections
    for acid_position in HHHH:
        for look_around in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
            if (acid_position[0] + look_around[0], acid_position[1] + look_around[1], acid_position[2] + look_around[2]) in HHHH:
                points += 1

    # finds all H-C and C-C connections
    for acid_position in CCCC:
        for look_around in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
            if (acid_position[0] + look_around[0], acid_position[1] + look_around[1], acid_position[2] + look_around[2]) in CCCC:
                points += 5
            elif (acid_position[0] + look_around[0], acid_position[1] + look_around[1], acid_position[2] + look_around[2]) in HHHH:
                points += 2

    # returns points scored by current fold
    return (points / 2) - protein.errorpoint[-1]
