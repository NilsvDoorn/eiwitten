from sys import argv
from protein import Protein
from option import Option
from field import Field
from path import Path
import time
import random
from copy import deepcopy
from math import ceil
from itertools import product

def main():
    """Asks for either 2D or 3D input, then uses the relevant code"""

    # checks whether program is used correctly
    check()

    if argv[2] == "3D":
        make_3D_fold()
    elif argv[2] == "2D":
        make_2D_fold()



def make_3D_fold():

    # Determines program running time
    start = time.time()

    # makes user input into the protein class
    protein = Protein(argv[1])

    options = Option()
    best_fold = options.options[0]
    best_positions = []
    ways = [["right"], ["forward"]]
    last_fold_points = 0
    AVG_points=0
<<<<<<< HEAD
=======
    P1 = 0.8
    P2 = 0.25
    # print(protein.lower_bound)
>>>>>>> 4ca0cbfe4b137045a2d908ab835e12e821c54864

    # creates fold based on the protein and the current option
    for aminoacid in range(len(protein.sequence) - 3):
        # round_points = []
        print('P1:', P1)
        print('AVG_points:', AVG_points)
        print('P2:', P2)
        print('last_fold_points:', last_fold_points)

        best_fold_points = 0
        new_ways = []
        round_points = 0
        print('aminoacid', aminoacid + 4)
        for route in ways:
            for option in options.options:
                route.append(option)
                if not options.mirror(route):
                    if options.3(protein.sequence[:aminoacid + 4], route):
                        pseudo_points = int(fold_points_3d(options.amino_positions(protein.sequence[:aminoacid + 4], route), protein.sequence) - protein.errorpoint[aminoacid + 3])
                        if aminoacid + 4 == protein.length:
                            if pseudo_points > best_fold_points:
                                best_fold_points = int(pseudo_points)
                                best_fold = deepcopy(route)
                        else:
                            if pseudo_points >= last_fold_points:
                                new_ways.append(deepcopy(route))
                                round_points += pseudo_points
                                if pseudo_points > best_fold_points:
                                    best_fold_points = pseudo_points
                            elif pseudo_points <= AVG_points:
                                # print('low chance')
                                if random.uniform(0,1) > P1:
                                    new_ways.append(deepcopy(route))
                                    round_points += pseudo_points
                            else:
                                # print('high chance')
                                if random.uniform(0,1) > P2:
                                    new_ways.append(deepcopy(route))
                                    round_points += pseudo_points
                route.pop()
        if not len(new_ways) == 0:
            AVG_points = round_points / len(new_ways)
        last_fold_points = best_fold_points
        ways = deepcopy(new_ways)
        print(len(ways))

    best_positions = options.amino_positions(protein.sequence, best_fold)
<<<<<<< HEAD
    

    # prints best_fold_points and best_fold and current field
=======
    # print("First best fold points: " + str(best_fold_points))
>>>>>>> 4ca0cbfe4b137045a2d908ab835e12e821c54864

    print(last_fold_points)
    print(best_fold)
    print(best_positions)
    end = time.time()
    print(end - start)

    print("This is best_positions: " + str(best_positions))
    print(best_positions[0])
    print(best_positions[0][2])

<<<<<<< HEAD
    # start visualisation
=======

    # start visualisation in 2D or 3D depending on version run
>>>>>>> 4ca0cbfe4b137045a2d908ab835e12e821c54864
    p = Path(protein.length, best_positions)
    if len(best_positions[0]) is 3:
        p.plot3Dfold(protein.sequence, best_fold_points)
    else:
        p.plotFold(protein.sequence, best_fold_points)

# checks user input
def check():
    if len(argv) != 3:
        exit("Usage: python versie0.py proteinsequence dimension")
    for aminoacid in argv[1]:
        if aminoacid != 'H' and aminoacid != 'P' and aminoacid != 'C':
            exit("Protein sequence can only contain P, C and H")
    for fold_dimension in argv[2]:
        if fold_dimension != "2D" and fold_dimension != "3D":
            exit("Please add either 2D or 3D as dimension for folding, after the given proteinsequence")

# checks the points scored by the current fold
def fold_points_3d(positions, sequence):
    points = 0
    HHHH = []
    CCCC = []
    for position, acid in zip(positions, sequence):
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
    return points / 2

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
            elif (acid_position[0] + look_around[0], acid_position[1] + look_around[1]) in CCCC:
                points += 1

    for acid_position in CCCC:
        for look_around in [[1,0],[-1,0],[0,1],[0,-1]]:
            if (acid_position[0] + look_around[0], acid_position[1] + look_around[1]) in CCCC:
                points += 5
            elif (acid_position[0] + look_around[0], acid_position[1] + look_around[1]) in HHHH:
                points += 1
    return points / 2

<<<<<<< HEAD
# def random_product(*args, repeat):
#     "Random selection from itertools.product(*args, **kwds)"
#     pools = [tuple(pool) for pool in args] * repeat
#     return tuple(random.choice(pool) for pool in pools)

def amino_positions_2D(sequence, option):
=======
def changed_amino_positions(sequence, option):
>>>>>>> 4ca0cbfe4b137045a2d908ab835e12e821c54864
    # initialises positions list and starting coordinates of protein
    positions = []
    begin = ceil(len(sequence) // 2)

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



if __name__ == '__main__':
    main()
