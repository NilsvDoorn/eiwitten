from sys import argv
from protein import Protein
from option import Option
from field import Field
from path import Path
import time
import random
from copy import deepcopy

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
    # prints best_fold_points and best_fold and current field
    best_positions = options.amino_positions(protein.sequence, best_fold)
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


if __name__ == '__main__':
    main()
