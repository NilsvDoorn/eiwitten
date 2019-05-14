from sys import argv
from protein import Protein
from random_option import Option
from field import Field
from path import Path
import time
import random
from copy import deepcopy
from math import ceil
from itertools import product

def main():
    # makes user input into the protein class
    protein = Protein(argv[1])

    options = Option(protein.length)
    best_fold = options.option
    best_positions = options.positions
    best_fold_points = fold_points(best_positions, protein.sequence) - protein.errorpoint[-1]

    possible_changes = list(product(["right", "left", "forward", "up", "down"], repeat = 7))

    for i in range(2):
        for index in range(len(protein.sequence) - 8):
            print("Hillclimber attempt number " + str(index + 1))
        # Iterates over all possible changes and adds them to every poiny in best_fold

            for change in possible_changes:
                changed_fold = best_fold

                changed_fold[index] = change[0]
                changed_fold[index + 1] = change[1]
                changed_fold[index + 2] = change[2]
                changed_fold[index + 3] = change[3]
                changed_fold[index + 4] = change[4]
                changed_fold[index + 5] = change[5]
                changed_fold[index + 6] = change[6]

                # Determines aminopositions of changed fold
                changed_positions = changed_amino_positions(protein.sequence, changed_fold)
                if changed_positions:
                    if (fold_points(changed_positions, protein.sequence)) - protein.errorpoint[-1] > best_fold_points:
                        print("New best fold points: ")
                        best_fold_points = fold_points(changed_positions, protein.sequence) - protein.errorpoint[-1]
                        best_fold = changed_fold
                        best_positions = changed_positions
                        print(best_fold_points)
                        print(best_fold)


    # prints best_fold_points and best_fold and current field
    print(best_fold_points)
    print(best_fold)
    print(best_positions)

    # renders visualisation
    p = Path(protein.length, best_positions)
    if best_positions[0][2]:
        p.plot3Dfold(protein.sequence, best_fold_points)
    else:
        p.plotFold(protein.sequence, best_fold_points)

# checks the points scored by the current fold
def fold_points(positions, sequence):
    points = 0
    HHHH = []
    CCCC = []
    for position, acid in zip(positions, sequence):
        if acid == "H":
            HHHH.append(position)
        elif acid == "C":
            CCCC.append(position)
    for i in range(len(HHHH)):
        if (HHHH[i][0] - 1, HHHH[i][1], HHHH[i][2]) in (HHHH or CCCC):
            points += 1
        if (HHHH[i][0], HHHH[i][1] - 1, HHHH[i][2]) in (HHHH or CCCC):
            points += 1
        if (HHHH[i][0], HHHH[i][1] + 1, HHHH[i][2]) in (HHHH or CCCC):
            points += 1
        if (HHHH[i][0] + 1, HHHH[i][1], HHHH[i][2]) in (HHHH or CCCC):
            points += 1
        if (HHHH[i][0], HHHH[i][1], HHHH[i][2] + 1) in (HHHH or CCCC):
            points += 1
        if (HHHH[i][0] + 1, HHHH[i][1], HHHH[i][2] - 1) in (HHHH or CCCC):
            points += 1
    for i in range(len(CCCC)):
        if (CCCC[i][0] - 1, CCCC[i][1], CCCC[i][2]) in CCCC:
            points += 5
        elif (CCCC[i][0] - 1, CCCC[i][1], CCCC[i][2]) in HHHH:
            points += 2
        if (CCCC[i][0], CCCC[i][1] - 1, CCCC[i][2]) in CCCC:
            points += 5
        elif (CCCC[i][0], CCCC[i][1] - 1, CCCC[i][2]) in HHHH:
            points += 2
        if (CCCC[i][0], CCCC[i][1] + 1, CCCC[i][2]) in CCCC:
            points += 5
        elif (CCCC[i][0], CCCC[i][1] + 1, CCCC[i][2]) in HHHH:
            points += 2
        if (CCCC[i][0] + 1, CCCC[i][1], CCCC[i][2]) in CCCC:
            points += 5
        elif (CCCC[i][0] + 1, CCCC[i][1], CCCC[i][2]) in HHHH:
            points += 2
        if (CCCC[i][0], CCCC[i][1], CCCC[i][2] + 1) in CCCC:
            points += 5
        elif (CCCC[i][0], CCCC[i][1], CCCC[i][2] + 1) in HHHH:
            points += 2
        if (CCCC[i][0], CCCC[i][1], CCCC[i][2] - 1) in CCCC:
            points += 5
        elif (CCCC[i][0], CCCC[i][1], CCCC[i][2] - 1) in HHHH:
            points += 2
    return points / 2

def changed_amino_positions(sequence, option):
    # initialises positions list and starting coordinates of protein
    positions = []
    begin = int(ceil(len(sequence) / 2))

    # initialises x-, y-coordinates and current direction
    x, y, z = begin, begin + 1, begin
    direction = "x_min"

    # loops over current option and appends aminoacid coordinates
    # if there are no bumps
    for move in option:
        if direction == "x_plus":
            if move == "right":
                y = y - 1
                direction = "y_min"
            elif move == "left":
                y = y + 1
                direction = "y_plus"
            elif move == "up":
                z = z + 1
                direction = "z_plus"
            elif move == "down":
                z = z - 1
                direction = "z_min"
            elif move == "forward":
                x = x + 1
        elif direction == "y_plus":
            if move == "right":
                x = x + 1
                direction = "x_plus"
            elif move == "left":
                x = x - 1
                direction = "x_min"
            elif move == "up":
                z = z + 1
                direction = "z_plus"
            elif move == "down":
                z = z - 1
                direction = "z_min"
            elif move == "forward":
                y = y + 1
        elif direction == "y_min":
            if move == "right":
                x = x - 1
                direction = "x_min"
            elif move == "left":
                x = x + 1
                direction = "x_plus"
            elif move == "up":
                z = z + 1
                direction = "z_plus"
            elif move == "down":
                z = z - 1
                direction = "z_min"
            elif move == "forward":
                y = y - 1
        elif direction == "x_min":
            if move == "right":
                y = y + 1
                direction = "y_plus"
            elif move == "left":
                y = y - 1
                direction = "y_min"
            elif move == "up":
                z = z + 1
                direction = "z_plus"
            elif move == "down":
                z = z - 1
                direction = "z_min"
            elif move == "forward":
                x = x - 1
        elif direction == "z_plus":
            if move == "right":
                x = x + 1
                direction = "x_plus"
            elif move == "left":
                x = x - 1
                direction = "x_min"
            elif move == "up":
                y = y + 1
                direction = "y_plus"
            elif move == "down":
                y = y - 1
                direction = "y_min"
            elif move == "forward":
                z = z + 1
        elif direction == "z_min":
            if move == "right":
                x = x + 1
                direction = "x_plus"
            elif move == "left":
                x = x - 1
                direction = "x_min"
            elif move == "up":
                y = y + 1
                direction = "y_plus"
            elif move == "down":
                y = y - 1
                direction = "y_min"
            elif move == "forward":
                z = z - 1
        # only appends coordinates if there are no bumps
        if tuple((x, y, z)) in positions:
            return False
        positions.append(tuple((x, y, z)))
    return positions

if __name__ == '__main__':
    main()
