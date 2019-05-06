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

    possible_changes = list(product(["right", "left", "forward"], repeat = 10))

    for index in range(len(protein.sequence) - 11):
        print("Hillclimber attempt number " + str(index))
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
            changed_fold[index + 7] = change[7]
            changed_fold[index + 8] = change[8]
            changed_fold[index + 9] = change[9]

            # Determines aminopositions of changed fold
            changed_positions = changed_amino_positions(protein.sequence, changed_fold)
            if changed_positions:
                if (fold_points(changed_positions, protein.sequence)) - protein.errorpoint[-1] > best_fold_points:
                    print("New best fold points: ")
                    best_fold_points = fold_points(changed_positions, protein.sequence) - protein.errorpoint[-1]
                    best_fold = changed_fold
                    best_positions = changed_positions
                    print(best_fold_points)


    # prints best_fold_points and best_fold and current field

    print(best_fold_points)
    print(best_fold)
    print(best_positions)

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
        if (HHHH[i][0] - 1, HHHH[i][1]) in (HHHH or CCCC):
            points += 1
        if (HHHH[i][0], HHHH[i][1] - 1) in (HHHH or CCCC):
            points += 1
        if (HHHH[i][0], HHHH[i][1] + 1) in (HHHH or CCCC):
            points += 1
        if (HHHH[i][0] + 1, HHHH[i][1]) in (HHHH or CCCC):
            points += 1
    for i in range(len(CCCC)):
        if (CCCC[i][0] - 1, CCCC[i][1]) in CCCC:
            points += 5
        elif (CCCC[i][0] - 1, CCCC[i][1]) in HHHH:
            points += 2
        if (CCCC[i][0], CCCC[i][1] - 1) in CCCC:
            points += 5
        elif (CCCC[i][0], CCCC[i][1] - 1) in HHHH:
            points += 2
        if (CCCC[i][0], CCCC[i][1] + 1) in CCCC:
            points += 5
        elif (CCCC[i][0], CCCC[i][1] + 1) in HHHH:
            points += 2
        if (CCCC[i][0] + 1, CCCC[i][1]) in CCCC:
            points += 5
        elif (CCCC[i][0] + 1, CCCC[i][1]) in HHHH:
            points += 2
    return points / 2

def changed_amino_positions(sequence, option):
    # initialises positions list and starting coordinates of protein
    positions = []
    begin = int(ceil(len(sequence) / 2))

    # appends first two positions to positions list
    positions.append(tuple((begin, begin)))
    positions.append(tuple((begin + 1, begin)))

    # initialises x-, y-coordinates and current direction
    x, y = begin, begin + 1
    direction = "d"

    # loops over current option and appends aminoacid coordinates
    # if there are no bumps
    for move in option:
        if direction == "d":
            if move == "right":
                x = x - 1
                direction = "l"
            elif move == "left":
                x = x + 1
                direction = "r"
            elif move == "forward":
                y = y + 1
        elif direction == "r":
            if move == "right":
                y = y + 1
                direction = "d"
            elif move == "left":
                y = y - 1
                direction = "u"
            elif move == "forward":
                x = x + 1
        elif direction == "l":
            if move == "right":
                y = y - 1
                direction = "u"
            elif move == "left":
                y = y + 1
                direction = "d"
            elif move == "forward":
                x = x - 1
        elif direction == "u":
            if move == "right":
                x = x + 1
                direction = "r"
            elif move == "left":
                x = x - 1
                direction = "l"
            elif move == "forward":
                y = y - 1
        # only appends coordinates if there are no bumps
        if tuple((y, x)) in positions:
            return False
        positions.append(tuple((y, x)))
    return positions



if __name__ == '__main__':
    main()
