import csv
import random
import time as timer
from protein import Protein
from path import Path
from copy import deepcopy
from functions import amino_positions_3d, fold_points_3d, mirror

def beam_search(sequence, chance_one, chance_two):

    # lets user know which program is currently being run
    print("__3D-Beam_Search__")

    # makes user input into the protein class
    protein = Protein(sequence)

    # begin timer for duration of algorithm
    start = timer.time()

    options = ["right", "forward", "left", "up", "down","back"]
    best_fold = options[0]
    best_positions = []

    ways = [["right"], ["forward"]]
    last_fold_points = 0
    AVG_points=0
    iterations = 0

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
                    coordinates_route = amino_positions_3d(route, False)

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
                            round_points += pseudo_points

                            # 100% proceeding, because higher compared to highest points last round
                            if pseudo_points >= last_fold_points:
                                new_ways.append(deepcopy(route))

                                if pseudo_points > best_fold_points:
                                    best_fold_points = pseudo_points

                            # lower as avarage last round, gets lower chance of proceeding
                            elif pseudo_points <= AVG_points:
                                if random.uniform(0,1) > chance_one:
                                    new_ways.append(deepcopy(route))

                            # higher as avarage last round, gets higher chance of proceeding
                            else:
                                if random.uniform(0,1) > chance_two:
                                    new_ways.append(deepcopy(route))

                route.pop()
        # can't divide by 0
        if not len(new_ways) == 0:
            AVG_points = round_points / len(new_ways)
        last_fold_points = best_fold_points
        ways = deepcopy(new_ways)
        iterations += len(ways)

    # end of algorithm, end time
    end = timer.time()
    time = round((end - start), 3)
    print("Score: " + str(int(best_fold_points)))

    # write results to relevant .csv file
    results = [protein.sequence,best_fold_points,time,chance_two,chance_one,iterations*5]
    with open('resultaten/3d/beam_search.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(results)
    csvFile.close()

    # # start visualisation in 2D or 3D depending on version run
    p = Path(protein.length, best_positions)
    p.plot3Dfold(protein.sequence, best_fold_points)

if __name__ == '__main__':
    beam_search()
