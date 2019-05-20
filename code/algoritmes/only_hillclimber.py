from sys import argv
from protein import Protein
from field import Field
from path import Path
import time
import random
from copy import deepcopy
from math import ceil
from itertools import product

change_length = 6
number_loops = 2

def hillclimber():
    # makes user input into the protein class
    protein = Protein(argv[1])

    # generates random viable option (no bumps)
    best_fold = list(random_product(["right", "left", "forward", "up", "down"], repeat = protein.length))
    while not amino_positions(best_fold):
        best_fold = list(random_product(["right", "left", "forward", "up", "down"], repeat = protein.length))

    # finds positions and fold points of randomly generated option
    best_positions = amino_positions(best_fold)
    best_fold_points = fold_points(best_positions, protein.sequence) - protein.errorpoint[-1]

    # creates list of all options of size change_length
    possible_changes = list(product(["forward", "left", "right", "up", "down"], repeat = change_length))

    # loops over entire protein number_loops' times
    for i in range(number_loops):
        for index in range(len(protein.sequence) - change_length):
            print("Hillclimber attempt number " + str(i + 1) + "." + str(index + 1))

            # iterates over all possible changes and adds them to every point in best_fold
            for change in possible_changes:
                changed_fold = deepcopy(best_fold)

                for change_index in range(change_length):
                    changed_fold[index + change_index] = change[change_index]

                # determines aminopositions of changed fold
                changed_positions = amino_positions(changed_fold)

                # remembers changed_fold and changed_positions if the score
                # is higher than that of best_fold
                if changed_positions:
                    if (fold_points(changed_positions, protein.sequence) - protein.errorpoint[-1]) > best_fold_points:
                        best_fold_points = fold_points(changed_positions, protein.sequence) - protein.errorpoint[-1]
                        best_fold = changed_fold
                        best_positions = changed_positions
                        print("New best fold points: " + str(int(best_fold_points)))
                        print("")


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

# from https://docs.python.org/3.1/library/itertools.html?highlight=combinations#itertools.product
# generates a random option of length protein.length
def random_product(*args, repeat):
    "Random selection from itertools.product(*args, **kwds)"
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(random.choice(pool) for pool in pools)

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
    for position in HHHH:
        if (position[0] - 1, position[1], position[2]) in (HHHH or CCCC):
            points += 1
        if (position[0], position[1] - 1, position[2]) in (HHHH or CCCC):
            points += 1
        if (position[0], position[1] + 1, position[2]) in (HHHH or CCCC):
            points += 1
        if (position[0] + 1, position[1], position[2]) in (HHHH or CCCC):
            points += 1
        if (position[0], position[1], position[2] + 1) in (HHHH or CCCC):
            points += 1
        if (position[0], position[1], position[2] - 1) in (HHHH or CCCC):
            points += 1
    for position in CCCC:
        if (position[0] - 1, position[1], position[2]) in CCCC:
            points += 5
        elif (position[0] - 1, position[1], position[2]) in HHHH:
            points += 2
        if (position[0], position[1] - 1, position[2]) in CCCC:
            points += 5
        elif (position[0], position[1] - 1, position[2]) in HHHH:
            points += 2
        if (position[0], position[1] + 1, position[2]) in CCCC:
            points += 2
        elif (position[0], position[1] + 1, position[2]) in HHHH:
            points += 2
        if (position[0] + 1, position[1], position[2]) in CCCC:
            points += 5
        elif (position[0] + 1, position[1], position[2]) in HHHH:
            points += 2
        if (position[0], position[1], position[2] + 1) in CCCC:
            points += 5
        elif (position[0], position[1], position[2] + 1) in HHHH:
            points += 2
        if (position[0], position[1], position[2] - 1) in CCCC:
            points += 5
        elif (position[0], position[1], position[2] - 1) in HHHH:
            points += 2
    return points / 2

def amino_positions(option):
    # initialises positions list and starting coordinates of protein
    positions = []
    begin = int(ceil(len(option) / 2))

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
    hillclimber()
