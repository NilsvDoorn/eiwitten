import sys
sys.path.insert(0,'../classes')
from protein import Protein
from path import Path

import csv
import random
import time as timer

from sys import argv
from copy import deepcopy

from functions import amino_positions_2d, fold_points_2d, mirror

def main():

    # makes user input into the protein class
    protein = Protein(argv[1])

    # begin timer for duration of algorithm
    start = timer.time()

    options = ["right", "forward", "left"]
    best_fold = options[0]
    best_positions = []

    ways = [["right"], ["forward"]]
    last_fold_points = 0
    AVG_points=0
    P1 = 0.8
    P2 = 0.25

    # creates fold based on the protein and the current option
    for aminoacid in range(len(protein.sequence) - 3):
        best_fold_points = 0
        new_ways = []
        all_ways = []
        round_points = 0
        for route in ways:
            for option in options:
                route.append(option)
                if not mirror(route):
                    coordinates_route = amino_positions_2d(route)
                    if coordinates_route:
                        pseudo_points = int(fold_points_2d(coordinates_route, protein.sequence) - protein.errorpoint[aminoacid + 3])
                        if aminoacid + 4 == protein.length:
                            if pseudo_points > best_fold_points:
                                best_fold_points = int(pseudo_points)
                                best_fold = deepcopy(route)
                                best_positions = coordinates_route
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



    end = timer.time()
    time = round((end - start), 3)

    results = [protein.sequence,best_fold_points,time,P2,P1]
    with open('beam.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(results)
    csvFile.close()

    # # start visualisation in 2D or 3D depending on version run
    p = Path(protein.length, best_positions)
    p.plotFold(protein.sequence, best_fold_points)

if __name__ == '__main__':
    main()
