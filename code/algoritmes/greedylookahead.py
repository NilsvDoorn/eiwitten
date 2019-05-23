from sys import argv
from protein import Protein
from option import Option
from path import Path
import time
from copy import deepcopy
from math import ceil
import csv



def main():
    """Asks for either 2D or 3D input, then uses the relevant code"""

    # checks whether program is used correctly
    check()

    # Determines program running time
    start = time.time()

    # set dimension for folding the protein
    dimension = argv[2]

    # makes user input into the protein class
    protein = Protein(argv[1])

    options = Option()
    best_fold = options.options[0]
    best_positions = []
    best_positions_2d = []
    ways = [["right"], ["forward"]]
    optellingwegens = 0
    # creates fold based on the protein and the current option

    if dimension == "3D":
        for aminoacid in range(len(protein.sequence) - 3):
            all_ways = []
            best_ways = []
            best_fold_points = 0
            print('aminoacid', aminoacid)
            for route in ways:
                for option in options.options:
                    route.append(option)
                    if not options.mirror(route):
                        coordinates_route = options.amino_positions(protein.sequence[:aminoacid + 4], route)
                        if coordinates_route:
                            pseudo_points = int(fold_points_3d(coordinates_route, protein.sequence) - protein.errorpoint[aminoacid + 3])
                            if aminoacid + 4 == protein.length:
                                if pseudo_points > best_fold_points:
                                    best_fold_points = int(pseudo_points)
                                    best_fold = deepcopy(route)
                                    best_coordinates = coordinates_route
                            elif aminoacid % 6 == 0:
                                if pseudo_points > best_fold_points:
                                    best_ways = []
                                    best_fold_points = pseudo_points
                                    best_ways.append(deepcopy(route))

                                elif pseudo_points == best_fold_points:
                                    best_ways.append(deepcopy(route))
                            else:
                                all_ways.append(deepcopy(route))
                    route.pop()
            if not len(best_ways) == 0:
                ways = deepcopy(best_ways)
            else:
                ways = deepcopy(all_ways)

            print(len(ways))
            optellingwegens += len(ways)

    # dimension == "2D"
    else:
        for aminoacid in range(len(protein.sequence) - 3):
            all_ways = []
            best_ways = []
            best_fold_points = 0
            print('aminoacid', aminoacid)
            for route in ways:
                for option in options.options_2D:
                    route.append(option)
                    if not options.mirror(route):
                        coordinates_route = amino_positions_2d(protein.sequence[:aminoacid + 4], route)
                        if coordinates_route:
                            pseudo_points = int(fold_points_2d(coordinates_route, protein.sequence) - protein.errorpoint[aminoacid + 3])
                            if aminoacid + 4 == protein.length:
                                if pseudo_points > best_fold_points:
                                    best_fold_points = int(pseudo_points)
                                    best_fold = deepcopy(route)
                                    best_coordinates = coordinates_route
                            elif aminoacid % 5 == 0:
                                if pseudo_points > best_fold_points:
                                    best_ways = []
                                    best_fold_points = pseudo_points
                                    best_ways.append(deepcopy(route))

                                elif pseudo_points == best_fold_points:
                                    best_ways.append(deepcopy(route))
                            else:
                                all_ways.append(deepcopy(route))
                    route.pop()


            if not len(best_ways) == 0:
                ways = deepcopy(best_ways)
            else:
                ways = deepcopy(all_ways)

            print(len(ways))
            optellingwegens += len(ways)

    # make positions sendig to matplotlib
    best_positions = best_coordinates

    end = time.time()
    tijd = end - start
    results = [protein.sequence,best_fold_points,round(tijd),optellingwegens*5]
    with open('greedylookahead.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(results)

    csvFile.close()

    print(best_fold)
    # start visualisation
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
    if argv[2] != "2D" and argv[2] != "3D":
            exit("Please add either 2D or 3D as dimension for folding, after the given proteinsequence")


# checks the points scored by the current 3D fold
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

    for acid_position in CCCC:
        for look_around in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
            if (acid_position[0] + look_around[0], acid_position[1] + look_around[1], acid_position[2] + look_around[2]) in CCCC:
                points += 5
            elif (acid_position[0] + look_around[0], acid_position[1] + look_around[1], acid_position[2] + look_around[2]) in HHHH:
                points += 2
    return points / 2


# checks the points scored by the current 3D fold
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


# amino positions function for 2D
def amino_positions_2d(sequence, option):
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
