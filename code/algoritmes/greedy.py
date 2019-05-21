from sys import argv
from protein import Protein
from path import Path
from copy import deepcopy
from functions import viable_random_product_3d, all_options_3d, amino_positions, fold_points_3d

change_length = 6
number_loops = 2

def greedy():
    # makes user input into the protein class
    protein = Protein(argv[1])

    # generates random viable option (no bumps)
    best_fold = viable_random_product_3d(change_length)

    # finds positions and fold points of randomly generated option
    best_positions = amino_positions(best_fold)
    best_fold_points = fold_points_3d(best_positions, protein, "change")

    # creates list of all options of size change_length
    possible_changes = all_options_3d(change_length)

    # loops over entire protein number_loops times
    for loop_number in range(number_loops):
        for index in range(len(protein.sequence) - change_length):

            # lets user know which loop is currently run
            loop = str(loop_number + 1) + "." + str(index + 1)
            print("Greedy attempt number " + loop)

            # tries all possibble changes on every point in best_fold
            for change in possible_changes:
                changed_fold = deepcopy(best_fold)
                for change_index in range(change_length):
                    changed_fold[index + change_index] = change[change_index]

                # determines aminopositions of changed fold
                changed_positions = amino_positions(changed_fold)

                # only checks score if there are no bumps
                if changed_positions:

                    # remembers fold and positions if they improve the score
                    fold_points = fold_points_3d(changed_positions, protein, "change")
                    if fold_points > best_fold_points:
                        best_fold_points = fold_points
                        best_fold = changed_fold
                        best_positions = changed_positions
                        print("New best fold points: " + str(int(best_fold_points)))
                        print("")

            # builds up the option on the first loop
            if (loop_number == 0):
                best_fold.append("forward")

    # renders visualisation
    p = Path(protein.length, best_positions)
    if best_positions[0][2]:
        p.plot3Dfold(protein.sequence, best_fold_points)
    else:
        p.plotFold(protein.sequence, best_fold_points)

if __name__ == '__main__':
    greedy()