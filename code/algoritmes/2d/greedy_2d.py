import sys
import time as timer

sys.path.insert(0,'../../classes')

from protein import Protein
from path import Path
from sys import argv
from copy import deepcopy
from functions_2d import viable_random_product_2d, all_options_2d, amino_positions_2d_hc, fold_points_2d_hc

change_length = 8
number_loops = 3

def greedy_2d():

    # lets user know which program is currently being run
    print("__2D-Greedy__")

    start = timer.time()

    # makes user input into the protein class
    protein = Protein(argv[1])

    # generates random viable option (no bumps)
    best_fold = viable_random_product_2d(change_length)

    # finds positions and fold points of randomly generated option
    best_positions = amino_positions_2d_hc(best_fold)
    best_fold_points = fold_points_2d_hc(best_positions, protein)

    # creates list of all options of size change_length
    possible_changes = all_options_2d(change_length)

    # loops over entire protein number_loops times
    for loop_number in range(number_loops):
        if loop_number == 0:
            print("Constructing...")
        else:
            print("Changing...")
        for index in range(len(protein.sequence) - change_length):

            # tries all possibble changes on every point in best_fold
            for change in possible_changes:
                changed_fold = deepcopy(best_fold)
                for change_index in range(change_length):
                    changed_fold[index + change_index] = change[change_index]

                # determines aminopositions of changed fold
                changed_positions = amino_positions_2d_hc(changed_fold)

                # only checks score if there are no bumps
                if changed_positions:

                    # remembers fold and positions if they improve the score
                    fold_points = fold_points_2d_hc(changed_positions, protein)
                    if fold_points > best_fold_points:
                        best_fold_points = fold_points
                        best_fold = changed_fold
                        best_positions = changed_positions

            # builds up the option on the first loop
            if (loop_number == 0):
                best_fold.append("forward")

    end = timer.time()
    time = round((end - start), 3)

    # write results to relevant .csv file
    results = [protein.sequence,best_fold_points,time]
    with open('../../../resultaten/2d/greedy_2d.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(results)
    csvFile.close()

    # lets user know the score of the best fold found
    print("Score: " + str(int(best_fold_points)))
    print("")

    # renders visualisation of the best fold found
    p = Path(protein.length, best_positions)
    p.plotFold(protein.sequence, best_fold_points)

if __name__ == '__main__':
    greedy_2d()
