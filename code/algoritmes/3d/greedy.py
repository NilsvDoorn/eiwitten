import sys
import csv
import time as timer

sys.path.insert(0,'../../classes')

from protein import Protein
from path import Path
from sys import argv
from copy import deepcopy
from functions import amino_positions_3d, fold_points_3d, mirror

def main():
    """Asks for either 2D or 3D input, then uses the relevant code"""

    # Determines program running time
    start = timer.time()

    # makes user input into the protein class
    protein = Protein(argv[1])

    options = ["right", "forward", "left", "up", "down", "back"]
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

                # ovoid mirror options
                if not mirror(route):
                    coordinates_route = amino_positions_3d(route)

                    # check for bumbs
                    if coordinates_route:

                        # calculate points of current fold
                        pseudo_points = int(fold_points_3d(coordinates_route, protein.sequence) - protein.errorpoint[aminoacid + 3])

                        # aminoacid + 4 is last route to add
                        if aminoacid + 4 == protein.length:
                            if pseudo_points > best_fold_points:
                                best_fold_points = int(pseudo_points)
                                best_fold = deepcopy(route)
                                best_positions = coordinates_route

                        else:
                            # if highest points so far, empty best_ways and append new best fold
                            if pseudo_points > best_fold_points:
                                best_ways = []
                                best_fold_points = pseudo_points
                                best_ways.append(deepcopy(route))

                            # equal to highest score proceeds as well
                            elif pseudo_points == best_fold_points:
                                best_ways.append(deepcopy(route))

                route.pop()
        if aminoacid % steps == 0:
            ways = deepcopy(best_ways)
        else:
            ways = deepcopy(all_ways)

        optellingwegens += len(ways)


    end = time.time()
    time = round((end - start), 3)

    # write results to relevant .csv file
    results = [protein.sequence, best_fold_points, time, optellingwegens*5]
    with open('../../../resultaten/3d/greedy.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(results)

    csvFile.close()

    # start visualisation
    p = Path(protein.length, best_positions)
    p.plot3Dfold(protein.sequence, best_fold_points)

if __name__ == '__main__':
    main()
