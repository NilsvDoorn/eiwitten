import sys
sys.path.insert(0,'../classes')
from protein import Protein
from path import Path

import time
import csv

from sys import argv
from copy import deepcopy

from functions import amino_positions_2d, fold_points_2d, mirror

def main():
    """Asks for either 2D or 3D input, then uses the relevant code"""

    # Determines program running time
    start = time.time()

    # makes user input into the protein class
    protein = Protein(argv[1])

    options = ["right", "forward", "left"]
    best_fold = options[0]

    best_positions = []
    best_positions_2d = []

    ways = [["right"], ["forward"]]
    optellingwegens = 0

    for aminoacid in range(len(protein.sequence) - 3):
        all_ways = []
        best_ways = []
        best_fold_points = 0
        print('aminoacid', aminoacid)
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


    end = time.time()
    tijd = end - start

    results = [protein.sequence, best_fold_points, round(tijd), optellingwegens*5]
    with open('greedylookahead.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(results)

    csvFile.close()

    print(best_fold)
    # start visualisation
    p = Path(protein.length, best_positions)
    p.plotFold(protein.sequence, best_fold_points)

if __name__ == '__main__':
    main()
