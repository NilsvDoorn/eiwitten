import sys
import csv
import random
import time as timer

sys.path.insert(0,'../classes')

from protein import Protein
from path import Path
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

    # chance of pruning a route
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

                # ovoid mirror options
                if not mirror(route):
                    coordinates_route = amino_positions_2d(route)

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
                            round_points += pseudo_points

                            # 100% proceeding, because higher compared to highest points last round
                            if pseudo_points >= last_fold_points:
                                new_ways.append(deepcopy(route))

                                if pseudo_points > best_fold_points:
                                    best_fold_points = pseudo_points

                            # lower as avarage last round, gets lower chance of proceeding
                            elif pseudo_points <= AVG_points:
                                if random.uniform(0,1) > P1:
                                    new_ways.append(deepcopy(route))

                            # higher as avarage last round, gets higher chance of proceeding
                            else:
                                if random.uniform(0,1) > P2:
                                    new_ways.append(deepcopy(route))

                route.pop()

        # can't divide by 0
        if not aminoacid + 4 == protein.length:
            AVG_points = round_points / len(new_ways)
        last_fold_points = best_fold_points
        ways = deepcopy(new_ways)

    # end of algorithm, end time
    end = timer.time()
    time = round((end - start), 3)

    # write results to the relevant .csv file
    results = [protein.sequence,best_fold_points,time,P2,P1]
    with open('beam_search_2d.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(results)
    csvFile.close()

    # # start visualisation in 2D or 3D depending on version run
    p = Path(protein.length, best_positions)
    p.plotFold(protein.sequence, best_fold_points)

if __name__ == '__main__':
    main()
