from sys import argv
from protein import Protein
from option import Option
from field import Field
import time
from copy import deepcopy

def main():
    start = time.time()
    # checks whether program is used correctly
    check()
    best_fold_points = 0
    # makes user input into the protein class
    protein = Protein(argv[1])
    # checks whether current option is better than all previous ones
    options = Option(protein.length)
    field = Field(protein.length, protein.sequence)
    best_fold = options.options[0]

    new_ways = [["right"], ["left"], ["forward"]]
    #
    ### while(not_all_options):
    #
    # creates field and fold based on the protein and the current option
    for aminoacid in range(len(protein.sequence) - 2):
        ways = deepcopy(new_ways)
        new_ways = []
        for option in options.options:
            for route in range(len(ways)):
                ways[route].append(option)
                if options.amino_positions(protein.sequence[:aminoacid + 4], ways[route]):
                    new_ways.append(deepcopy(ways[route]))
                    # print("new", new_ways)

                    # check wether current fold is the best and remembers it if it is
                    if fold_points(options.amino_positions(protein.sequence[:aminoacid + 4], ways[route]), protein.sequence) > best_fold_points:
                        best_fold_points = fold_points(options.amino_positions(protein.sequence[:aminoacid + 4], ways[route]), protein.sequence)
                        best_fold = deepcopy(ways[route])
                        best_positions = options.amino_positions(protein.sequence[:aminoacid + 4], ways[route])
                        # print(best_fold)
                # print("before pop new", new_ways)
                ways[route].pop()
                # print("after new", new_ways)
    # prints best_fold_points and best_fold and current field
    print(best_fold_points - protein.errorpoint)
    print(best_fold)
    print(best_positions)
    field.fill_field(best_positions, protein.sequence)
    print("Field:")
    for line in field.field:
        print(line)
    end = time.time()
    print(end - start)

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
    for i in range(len(CCCC)):
        if (CCCC[i][0] - 1, CCCC[i][1]) in CCCC:
            points += 5
        elif (CCCC[i][0] - 1, CCCC[i][1]) in HHHH:
            points += 1
        if (CCCC[i][0], CCCC[i][1] - 1) in CCCC:
            points += 5
        elif (CCCC[i][0], CCCC[i][1] - 1) in HHHH:
            points += 1
    return points


if __name__ == '__main__':
    main()
