import random
from math import ceil
from itertools import product

# from https://docs.python.org/3.1/library/itertools.html?highlight=combinations#itertools.product
# generates a random option of length protein.length
def random_product(*args, repeat):
    "Random selection from itertools.product(*args, **kwds)"
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(random.choice(pool) for pool in pools)

def viable_random_product(length):
    best_fold = list(random_product(["right", "left", "forward", "up", "down"], repeat = length))
    while not amino_positions(best_fold):
        best_fold = list(random_product(["right", "left", "forward", "up", "down"], repeat = length))
    return best_fold

def all_options_3d(length):
    return list(product(["forward", "left", "right", "up", "down"], repeat = length))

def amino_positions(option):
    # initialises positions list and starting coordinates of protein
    positions = []
    begin = int(ceil(len(option) / 2))

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

# checks the points scored by the current fold
def fold_points_3d(positions, protein, version):
    points = 0
    HHHH = []
    CCCC = []
    for position, acid in zip(positions, protein.sequence):
        if acid == "H":
            HHHH.append(position)
        elif acid == "C":
            CCCC.append(position)
    for acid_position in HHHH:
        for look_around in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
            if (acid_position[0] + look_around[0], acid_position[1] + look_around[1], acid_position[2] + look_around[2]) in HHHH:
                points += 1
            elif (acid_position[0] + look_around[0], acid_position[1] + look_around[1], acid_position[2] + look_around[2]) in CCCC:
                points += 1

    for acid_position in CCCC:
        for look_around in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
            if (acid_position[0] + look_around[0], acid_position[1] + look_around[1], acid_position[2] + look_around[2]) in CCCC:
                points += 5
            elif (acid_position[0] + look_around[0], acid_position[1] + look_around[1], acid_position[2] + look_around[2]) in HHHH:
                points += 1
    if version == "change":
        return (points / 2) - protein.errorpoint[-1]
    else:
        return points / 2
