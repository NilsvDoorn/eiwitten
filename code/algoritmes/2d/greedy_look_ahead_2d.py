import csv
import time as timer
from protein import Protein
from path import Path
from copy import deepcopy
from functions_2d import all_options_2d, amino_positions_2d, fold_points_2d

def greedy_look_ahead_2d(sequence, change_length, number_loops):

    # lets user know which program is currently being run
    print("__2D-Greedy with look ahead__")

    # determines algorithm running time
    start = timer.time()

    # makes user input into the protein class
    protein = Protein(sequence)

    # creates list of all options of size change_length
    possible_changes = list(all_options_2d(change_length))
    for i in possible_changes:
        print(i)

    # takes first option from possible_changes and finds positions and points
    best_fold = list(possible_changes[0])
    best_positions = amino_positions_2d(best_fold, True)
    best_fold_points = fold_points_2d(best_positions, protein.sequence) - protein.errorpoint[-1]

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
                changed_positions = amino_positions_2d(changed_fold, True)

                # only checks score if there are no bumps
                if changed_positions:

                    # remembers fold and positions if they improve the score
                    fold_points = fold_points_2d(changed_positions, protein.sequence) - protein.errorpoint[-1]
                    if fold_points > best_fold_points:
                        best_fold_points = fold_points
                        best_fold = changed_fold
                        best_positions = changed_positions

            # builds up the option on the first loop
            if loop_number == 0:
                best_fold.append("forward")

    # determines running time of greedy with look ahead algorithm
    end = timer.time()
    time = round((end - start), 3)

    # write results to relevant .csv file
    results = [protein.sequence,best_fold_points,time]
    with open('resultaten/2d/greedylookahead_2d.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(results)
    csvFile.close()

    # lets user know the score of the best fold found
    print("Score: " + str(int(best_fold_points)))

    # renders visualisation of the best fold found
    p = Path(protein.length, best_positions)
    p.plotFold(protein.sequence, best_fold_points)

if __name__ == '__main__':
    greedy_look_ahead_2d()
