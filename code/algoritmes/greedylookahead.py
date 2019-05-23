from sys import argv
from protein import Protein
from path import Path
import time
from copy import deepcopy
from math import ceil
from functions import amino_positions_2d, amino_positions_3d, fold_points_2d, fold_points_3d, mirror
import csv


def main():
    """Asks for either 2D or 3D input, then uses the relevant code"""

    # Determines program running time
    start = time.time()

    # set dimension for folding the protein
    dimension = argv[2]

    # makes user input into the protein class
    protein = Protein(argv[1])

    if dimension == "3D":
        options = ["right", "forward", "left", "up", "down", "back"]
    elif dimension == "2D":
        options = ["right", "forward", "left"]
    best_fold = options[0]

    best_positions = []
    best_positions_2d = []

    ways = [["right"], ["forward"]]
    optellingwegens = 0

    if dimension == "3D":
        for aminoacid in range(len(protein.sequence) - 3):
            all_ways = []
            best_ways = []
            best_fold_points = 0
            print('aminoacid', aminoacid)
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

    results = [protein.sequence, best_fold_points, round(tijd), optellingwegens*5]
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

if __name__ == '__main__':
    main()
