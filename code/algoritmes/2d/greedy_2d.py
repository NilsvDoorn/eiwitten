import csv
import time as timer
from protein import Protein
from path import Path
from copy import deepcopy
from functions_2d import all_options_2d, amino_positions_2d, fold_points_2d, mirror

def greedy_2d(sequence):

    # lets user know which program is currently being run
    print("__2D-Greedy__")

    # Determines program running time
    start = timer.time()

    # makes user input into the protein class
    protein = Protein(sequence)

    options = ["right", "forward", "left"]
    best_fold = options[0]

    best_positions = []
    best_positions_2d = []

    ways = [["right"], ["forward"]]
    iterations = 0

    for aminoacid in range(len(protein.sequence) - 3):
        best_ways = []
        best_fold_points = -1
        print('Aminoacid:', aminoacid + 1)
        for route in ways:
            for option in options:
                route.append(option)

                # ovoid mirror options
                if not mirror(route):
                    coordinates_route = amino_positions_2d(route, False)

                    # check for bumbs
                    if coordinates_route:

                        # calculate points of current fold
                        pseudo_points = int(fold_points_2d(coordinates_route, protein.sequence) - protein.errorpoint[aminoacid + 3])

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

                            # folds equal to the highest score proceeds as well
                            elif pseudo_points == best_fold_points:
                                best_ways.append(deepcopy(route))

                route.pop()

        ways = deepcopy(best_ways)
        if len(ways) == 0 and not aminoacid + 4 == protein.length:
            exit("Geen vouwing mogelijk doordat het algoritme zich heeft ingebouwd")
        print("Constructing...")
        iterations += len(ways)


    end = timer.time()
    time = round((end - start), 3)
    print("Score: " + str(int(best_fold_points)))
    # write results to relevant .csv file
    results = [protein.sequence, best_fold_points, time, iterations*5]
    with open('resultaten/2d/greedy_2d.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(results)

    csvFile.close()

    # start visualisation
    p = Path(protein.length, best_positions)
    p.plotFold(protein.sequence, best_fold_points)

if __name__ == '__main__':
    greedy_2d()
