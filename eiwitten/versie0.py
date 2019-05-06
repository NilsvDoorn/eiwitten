from sys import argv
from protein import Protein
from option import Option
from field import Field
from path import Path
import time
import random
from copy import deepcopy
from math import ceil
from itertools import product

def main():
    start = time.time()
    # checks whether program is used correctly
    check()

    # makes user input into the protein class
    protein = Protein(argv[1])

    options = Option(protein.length)
    best_fold = options.options[0]
    best_positions = [(0, 0), (0, 1)]

    ways = [["right"], ["forward"]]
    last_fold_points = 0
    P1 = 0.8
    P2 = 0.5

    # creates field and fold based on the protein and the current option
    for aminoacid in range(len(protein.sequence) - 3):
        best_fold_points = 0
        new_ways = []
        print('aminoacid', aminoacid)

        for route in ways:
            for option in options.options:
                route.append(option)
                if not options.mirror(route):
                    if options.amino_positions(protein.sequence[:aminoacid + 4], route):
                        pseudo_points = fold_points(options.amino_positions(protein.sequence[:aminoacid + 4], route), protein.sequence) - protein.errorpoint[aminoacid + 3]
                        if aminoacid + 4 == protein.length:
                            if pseudo_points > best_fold_points:
                                best_fold_points = pseudo_points
                                best_fold = deepcopy(route)
                        else:
                            if pseudo_points >= last_fold_points:
                                new_ways.append(deepcopy(route))
                                if pseudo_points > best_fold_points:
                                    best_fold_points = pseudo_points
                            elif pseudo_points < protein.lower_bound[aminoacid + 3]:
                                if random.uniform(0,1) > P1:
                                    new_ways.append(deepcopy(route))
                            else:
                                if random.uniform(0,1) > P2:
                                    new_ways.append(deepcopy(route))
                route.pop()
        ways = deepcopy(new_ways)
        if not best_fold_points == 0:
            last_fold_points = best_fold_points
        print(len(ways))
        # for i in ways:
        #     print(i)
        # print("")
                # print("after new", new_ways)

    best_positions = options.amino_positions(protein.sequence, best_fold)
    print("First best fold points: " + str(best_fold_points))

    error = protein.errorpoint[-1]

    for index in range(len(protein.sequence) - 12):
        print("Hillclimber attempt number " + str(index))
        changed_fold = best_fold
        possible_changes = list(product(["right", "left", "up", "down"], repeat = 10))
        for change in possible_changes:
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
            changed_positions = changed_amino_positions(protein.sequence, changed_fold)
            if changed_positions and (fold_points(changed_positions, protein.sequence)) - error > last_fold_points:
                print("New best fold points: ")
                last_fold_points = fold_points(changed_positions, protein.sequence) - error
                best_fold = changed_fold
                best_positions = changed_positions
                print(last_fold_points)

    # prints best_fold_points and best_fold and current field

    print(last_fold_points)
    print(best_fold)
    print(best_positions)
    field = Field(protein.length, protein.sequence)
    field.fill_field(best_positions, protein.sequence)
    print("Field:")
    for line in field.field:
        print(line)
    end = time.time()
    print(end - start)

    # start visualisation
    p = Path(protein.length, best_positions)
    #if best_positions[0][2]:
    #    p.plot3Dfold(protein.sequence)
    #else:
    p.plotFold(protein.sequence)

# checks user input
def check():
    if len(argv) != 2:
        exit("Usage: python versie0.py proteinsequence")
    for aminoacid in argv[1]:
        if aminoacid != 'H' and aminoacid != 'P' and aminoacid != 'C':
            exit("Protein sequence can only contain P, C and H")

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

def random_product(*args, repeat):
    "Random selection from itertools.product(*args, **kwds)"
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(random.choice(pool) for pool in pools)

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
