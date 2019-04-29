from sys import argv
from protein import Protein
from option import Option
from field import Field
import time


def fold_points(positions, sequence):
    points = 0
    HHHH = []
    CCCC = []
    print(positions)
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

def main():
    start= time.time()
    # checks whether program is used correctly
    check()

    # makes user input into the protein class
    protein = Protein(argv[1])

    # creates howmanyoptions number of options and remembers which is best
    howmanyoptions = 1000
    best_fold_points = 0
    second_best_fold_points = 0
    actualbestfold = []
    actualbestoption = []
    previousoptions = []
    for i in range(howmanyoptions):
        # generates random, viable option and determines its point value
        option = Option(protein.length, protein.sequence)
        if option.option not in previousoptions:
            previousoptions.append(option.option)
            # checks whether current option is best and remembers if it is
            if int(option.points) > best_fold_points:
                if best_fold_points != 0 :
                    second_best_fold_points = best_fold_points
                    second_best_fold = best_fold
                    second_best_option = best_option
                best_fold_points = option.points
                best_fold = option.positions
                best_option = option.option
            elif option.points > second_best_fold_points:
                second_best_fold_points = option.points
                second_best_fold = option.positions
                second_best_option = option.option
        else:
            print("XXXXX")


    for i,j,k,l,m in zip(best_option, best_fold, second_best_option, second_best_fold, range(len(best_option))):
        if m < (len(best_option) / 2):
            actualbestfold.append(j)
            actualbestoption.append(i)
        else:
            actualbestfold.append(l)
            actualbestoption.append(k)


    if fold_points(actualbestfold, protein.sequence) > best_fold_points:
        print("XXX")
        best_option = actualbestoption
        best_fold = actualbestfold
        best_fold_points = fold_points(actualbestfold, protein.sequence)


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
