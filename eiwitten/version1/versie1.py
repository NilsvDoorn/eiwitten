from sys import argv
from protein import Protein
from option import Option
from field import Field
import time


def main():
    start= time.time()
    # checks whether program is used correctly
    check()
    best_fold_points = 0

    # makes user input into the protein class
    protein = Protein(argv[1])

    # creates howmanyoptions number of options and remembers which is best
    howmanyoptions = 1000
    for i in range(howmanyoptions):
        # generates random, viable option and determines its point value
        option = Option(protein.length, protein.sequence)
        # checks whether current option is best and remembers if it is
        if int(option.points) > best_fold_points:
            best_fold_points = option.points
            best_fold = option.positions
            best_option = option.option

    # prints best fold, best fold points and best fold positions
    print(best_option)
    print(best_fold)
    print(best_fold_points - protein.errorpoint)

    # creates and prints field based on best fold
    field = Field(protein.length)
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

if __name__ == '__main__':
    main()
