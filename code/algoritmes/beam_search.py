from sys import argv
from protein import Protein
from path import Path
import time
import random
from copy import deepcopy
from math import ceil
from itertools import product
import csv

def main():

    # determines program running time
    start = time.time()

    # checks whether program is used correctly
    check()

    # makes user input into the protein class
    protein = Protein(argv[1])

    options = ["right", "forward", "left", "up", "down"]
    best_fold = options[0]
    best_positions = []

    ways = [["right"], ["forward"]]
    last_fold_points = 0
    AVG_points=0
<<<<<<< HEAD:code/algoritmes/versie0.py
    P1 = 0.8
    P2 = 0.25
    # print(protein.lower_bound)
=======
    P1 = 0.9
    P2 = 0.5
>>>>>>> d2a2a32729c078f4d3db2ccaab8dfdfabb9c6f86:code/algoritmes/beam_search.py

    # creates fold based on the protein and the current option
    for aminoacid in range(len(protein.sequence) - 3):
        # round_points = []
        best_fold_points = 0
        new_ways = []
        all_ways = []
        round_points = 0
        # print('aminoacid', aminoacid + 4)
        for route in ways:
            for option in options:
                route.append(option)
                if not mirror(route):
                    coordinates_route = options.amino_positions(protein.sequence[:aminoacid + 4], route)
                    if coordinates_route:
                        pseudo_points = int(fold_points_3d(coordinates_route, protein.sequence) - protein.errorpoint[aminoacid + 3])
                        if aminoacid + 4 == protein.length:
                            if pseudo_points > best_fold_points:
                                best_fold_points = int(pseudo_points)
                                best_fold = deepcopy(route)
                        else:
                            round_points += pseudo_points
                            if pseudo_points >= last_fold_points:
                                new_ways.append(deepcopy(route))

                                if pseudo_points > best_fold_points:
                                    best_fold_points = pseudo_points
                            elif pseudo_points <= AVG_points:
                                if random.uniform(0,1) > P1:
                                    new_ways.append(deepcopy(route))

                            else:
                                if random.uniform(0,1) > P2:
                                    new_ways.append(deepcopy(route))

                route.pop()
        if not len(new_ways) == 0:
            AVG_points = round_points / len(new_ways)
        last_fold_points = best_fold_points
        ways = deepcopy(new_ways)
        # print(len(ways))

    best_positions = amino_positions(protein.sequence, best_fold)

<<<<<<< HEAD:code/algoritmes/versie0.py
    # print(last_fold_points)
    # print(best_fold)
    # print(best_positions)
=======
>>>>>>> d2a2a32729c078f4d3db2ccaab8dfdfabb9c6f86:code/algoritmes/beam_search.py
    end = time.time()
    tijd = end - start
    # print(time)

    # print("This is best_positions: " + str(best_positions))
    # print(best_positions[0])
    # print(best_positions[0][2])
    results = [protein.sequence,best_fold_points,round(tijd),P2,P1]
    with open('beam.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(results)

    csvFile.close()
    # # start visualisation in 2D or 3D depending on version run
    # p = Path(protein.length, best_positions)
    # if len(best_positions[0]) is 3:
    #     p.plot3Dfold(protein.sequence, best_fold_points)
    # else:
    #     p.plotFold(protein.sequence, best_fold_points)

# checks user input
def check():
    if len(argv) != 2:
        exit("Usage: python versie0.py proteinsequence")
    for aminoacid in argv[1]:
        if aminoacid != 'H' and aminoacid != 'P' and aminoacid != 'C':
            exit("Protein sequence can only contain P, C and H")

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

    for acid_position in CCCC:
        for look_around in [[1,0],[-1,0],[0,1],[0,-1]]:
            if (acid_position[0] + look_around[0], acid_position[1] + look_around[1]) in CCCC:
                points += 5
            elif (acid_position[0] + look_around[0], acid_position[1] + look_around[1]) in HHHH:
                points += 2
    return points / 2

def changed_amino_positions(sequence, option):
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

def mirror(route):
    for option in route:
        if option == 'right':
            return False
        elif option == 'left' or option == "up" or option == "down":
            return True
    return True

def amino_positions(sequence, option):
    # initialises positions list and starting coordinates of protein
    positions = []
    begin = int(ceil(len(sequence) / 2))

    # appends first two positions to positions list
    positions.append(tuple((begin, begin, begin)))
    positions.append(tuple((begin, begin + 1, begin)))

    # initialises x-, y- and z-coordinates and current direction
    x, y, z = begin, begin + 1, begin
    directions = {'y_plus':{'right': [1,0,0,'x_min'], 'left': [-1,0,'x_plus'], 'forward': [0,-1]},
                'x_plus':{'right': [0,-1,0,'y_min'], 'left': [0,1,0,'y_plus'], 'up': [0,0,1,'z_plus'], 'down': [0,0,-1,'z_min'], 'forward': [1,0,0,'x_plus']},
                'x_min':{'right': [0,1,'y_plus'], 'left': [0,-1,'y_min'], 'forward': [1,0]},
                'y_min':{'right': [-1,0,'x_plus'], 'left': [1,0,'x_min'], 'forward': [0,1]},
                'z_plus':{'right': [-1,0,'x_plus'], 'left': [1,0,'x_min'], 'forward': [0,1]},
                'z_min':{'right': [-1,0,'x_plus'], 'left': [1,0,'x_min'], 'forward': [0,1]}}
    direction = "y_min"

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
        elif direction == "y_min":
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
        elif direction == "y_plus":
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


if __name__ == '__main__':
    main()
