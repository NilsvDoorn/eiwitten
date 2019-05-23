import random
import csv
import time as timer
from protein import Protein
from path import Path
from copy import deepcopy
from functions_2d import amino_positions_2d, fold_points_2d, mirror

<<<<<<< HEAD:code/algoritmes/2d/greedylookahead_beam_2d.py
def main():
    # lets user know which program is currently being run
    print("__2D-Greedylookahead_with_Beam_Search__")
=======
def greedy_look_ahead_beam_2d(sequence):
>>>>>>> 9e919eec05dd6f29a2491c8c6b04a3789234a742:code/algoritmes/2d/greedy_look_ahead_beam_2d.py

    # Determines program running time
    start = timer.time()

    # makes user input into the protein class
    protein = Protein(sequence)

    options = ["right", "forward", "left"]
    best_fold = options[0]
    best_positions = []

    ways = [["right"], ["forward"]]
    last_fold_points = 0
    AVG_points=0

    # chance to prune a fold
    P1 = 1
    P2 = 1

    # steps to look ahead
    steps = 6

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

                        # look ahead steps aminoacids
                        elif aminoacid % steps == 0:

                            # if highest points so far, empty best_ways and append new best fold
                            if pseudo_points > best_fold_points:

                                # give last best score a chance to proceed
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

                            # equal to highest score proceeds as well
                            elif pseudo_points == best_fold_points:
                                best_ways.append(deepcopy(route))

                            # low chance of proceeding
                            elif pseudo_points <= AVG_points:
                                if random.uniform(0,1) > P1:
                                    new_ways.append(deepcopy(route))

                            # high chance of proceeding
                            else:
                                if random.uniform(0,1) > P2:
                                    new_ways.append(deepcopy(route))

                        # remember all folds
                        else:
                            round_points += pseudo_points
                            all_ways.append(deepcopy(route))
                route.pop()

        if aminoacid % steps == 0:
            for i in best_ways:
                new_ways.append(deepcopy(i))
            ways = deepcopy(new_ways)
        elif not len(all_ways) == 0:
            AVG_points = round_points / len(all_ways)
            ways = deepcopy(all_ways)

        optellingwegens += len(ways)

    end = timer.time()
    time = round((end - start), 3)

    # write results to relevant .csv file
    results = [protein.sequence, best_fold_points, time, P2, P1, optellingwegens*5]
    with open('resultaten/2d/greedylookahead_beam_2d.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(results)

    csvFile.close()

    # start visualisation
    p = Path(protein.length, best_positions)
    p.plotFold(protein.sequence, best_fold_points)

if __name__ == '__main__':
    greedylookahead_beam_2d()