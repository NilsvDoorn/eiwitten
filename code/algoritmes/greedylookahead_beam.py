import sys
sys.path.insert(0,'../classes')
from protein import Protein
from path import Path


import time
import random
import csv

from sys import argv
from copy import deepcopy
from functions import amino_positions_3d, fold_points_3d, mirror


def main():

    # Determines program running time
    start = time.time()

    # makes user input into the protein class
    protein = Protein(argv[1])

    options = ["right", "forward", "left", "up", "down", "back"]
    best_fold = options[0]
    best_positions = []

    ways = [["right"], ["forward"]]
    last_fold_points = 0
    AVG_points=0
    P1 = 1
    P2 = 1
    optellingwegens = 0
    # creates fold based on the protein and the current option
    for aminoacid in range(len(protein.sequence) - 3):
        best_fold_points = 0
        new_ways = []
        all_ways = []
        best_ways = []
        round_points = 0
        # print('aminoacid', aminoacid)
        for route in ways:
            for option in options:
                route.append(option)
                if not mirror(route):
                    coordinates_route = amino_positions_3d(route)
                    if coordinates_route:
                        pseudo_points = int(fold_points_3d(coordinates_route, protein.sequence) - protein.errorpoint[aminoacid + 3])

                        if aminoacid + 4 == protein.length:
                            if pseudo_points > best_fold_points:
                                best_fold_points = int(pseudo_points)
                                best_fold = deepcopy(route)
                        elif aminoacid % 7 == 0:
                            if pseudo_points > best_fold_points:
                                for i in best_ways:
                                    if pseudo_points <= AVG_points:
                                        if random.uniform(0,1) > P1:
                                            new_ways.append(deepcopy(i))
                                    else:
                                        if random.uniform(0,1) > P2:
                                            new_ways.append(deepcopy(i))
                                best_ways = []
                                best_fold_points = pseudo_points
                                best_ways.append(deepcopy(route))

                            elif pseudo_points == best_fold_points:
                                best_ways.append(deepcopy(route))

                            elif pseudo_points <= AVG_points:
                                if random.uniform(0,1) > P1:
                                    new_ways.append(deepcopy(route))
                            else:
                                if random.uniform(0,1) > P2:
                                    new_ways.append(deepcopy(route))
                        else:
                            round_points += pseudo_points
                            all_ways.append(deepcopy(route))
                route.pop()
        for i in best_ways:
            new_ways.append(deepcopy(i))

        if not len(new_ways) == 0:
            ways = deepcopy(new_ways)
        elif not len(all_ways) == 0:
            AVG_points = round_points / len(all_ways)
            ways = deepcopy(all_ways)

        # print(len(ways))
        optellingwegens += len(ways)

    # make positions sendig to matplotlib
    best_positions = amino_positions_3d(best_fold)

    end = time.time()
    tijd = end - start
    results = [protein.sequence,best_fold_points,round(tijd),P2,P1,optellingwegens*5]
    with open('greedylookahead_beam.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(results)

    csvFile.close()

    # start visualisation
    p = Path(protein.length, best_positions)
    if len(best_positions[0]) is 3:
        p.plot3Dfold(protein.sequence, best_fold_points)
    else:
        p.plotFold(protein.sequence, best_fold_points)

if __name__ == '__main__':
    main()
