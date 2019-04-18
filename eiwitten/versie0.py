from sys import argv
from protein import Protein
from option import Option
from field import Field
import time
from copy import deepcopy

def main():
    start= time.time()
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
    for aminoacid in range(len(protein.sequence) - 3):
        ways = deepcopy(new_ways)
        # print("ways", ways)
        new_ways = []
        for option in options.options:
            for route in range(len(ways)):
                ways[route].append(option)
                if field.fill_field(protein.sequence[:aminoacid + 4], ways[route]):
                    new_ways.append(deepcopy(ways[route]))
                    # print("new", new_ways)

                    # check wether current fold is the best and remembers it if it is
                    if fold_points(field) > best_fold_points:
                        best_fold_points = fold_points(field)
                        best_fold = deepcopy(ways[route])
                        # print(best_fold)
                field.clear_field(protein.length)
                field.x_cdn = protein.length - 1
                field.y_cdn = protein.length
                # print("before pop new", new_ways)
                ways[route].pop()
                # print("after new", new_ways)
    # prints best_fold_points and best_fold and current field
    print(best_fold_points - protein.errorpoint)
    print(best_fold)
    field.fill_field(protein.sequence, best_fold)
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
def fold_points(field):
    points = 0
    for i in range(field.dimension):
       for j in range(field.dimension):
           if field.field[j][i] == "H":
               for k in [[1,0],[0,-1]]:
                   if field.field[j + k[0]][i + k[1]] == "H":
                       points += 1
           elif field.field[j][i] == "C":
                for k in [[1,0],[0,-1]]:
                    if field.field[j + k[0]][i + k[1]] == "C":
                        points += 5
    return(points)


if __name__ == '__main__':
    main()
