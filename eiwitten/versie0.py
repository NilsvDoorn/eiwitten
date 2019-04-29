from sys import argv
from protein import Protein
from option import Option
from field import Field
# from path import Path
# import Tkinter as tk
import time
import random
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from copy import deepcopy

def main():
    all= time.time()
    start= time.time()
    # checks whether program is used correctly
    check()
    best_fold_points = 0
    # makes user input into the protein class
    protein = Protein(argv[1])
    options = Option(protein.length)
    field = Field(protein.length, protein.sequence)
    ways = [["right"], ["forward"]]
    last_fold_points = 0
    P1 = 1
    P2 = 0.9

    # creates field and fold based on the protein and the current option
    for aminoacid in range(len(protein.sequence) - 3):
        best_fold_points = 0
        end = time.time()
        # print(end - start)
        start = time.time()
        print(aminoacid, "amino")
        new_ways = []
        all_ways = []
        # last_fold_points = protein.lower_bound[aminoacid + 3]
        for route in ways:
            for option in options.options:
                route.append(option)
                if not options.mirror(route): # and not options.PPP(protein.sequence, route):
                    if field.fill_field(protein.sequence[:aminoacid + 4], route):
                        pseudo_points = fold_points(field) - protein.errorpoint[aminoacid + 3]
                        if aminoacid + 4 == protein.length:
                            if pseudo_points > best_fold_points:
                                best_fold_points = pseudo_points
                                best_fold = deepcopy(route)

                        # check wether current fold is the best and remembers it if it is
                        elif protein.sequence[aminoacid + 3] == 'H' or protein.sequence[aminoacid + 3] == 'C':
                            if  pseudo_points >= last_fold_points:
                                new_ways.append(deepcopy(route))
                                if pseudo_points > best_fold_points:
                                    best_fold_points = pseudo_points
                            elif pseudo_points < protein.lower_bound[aminoacid + 3]:
                                if random.uniform(0, 1) > P1:
                                    new_ways.append(deepcopy(route))
                            else:
                                if random.uniform(0, 1) > P2:
                                    new_ways.append(deepcopy(route))

                        else:
                            all_ways.append(deepcopy(route))
                    # print("before pop new", new_ways)
                    field.clear_field(protein.length)
                    field.x_cdn = protein.length - 1
                    field.y_cdn = protein.length
                route.pop()


        if not len(new_ways) == 0 or aminoacid + 4 == protein.length:
            print("New")
            ways = deepcopy(new_ways)
        else:
            print("All")
            ways = deepcopy(all_ways)
            best_fold_points = last_fold_points
        for i in ways:
            print(i)
        last_fold_points = best_fold_points

    field.fill_field(protein.sequence, best_fold)
    print(best_fold_points)
    print(best_fold)
    for line in field.field:
        print(line)
    end = time.time()
    print(end - all)

    # # start visualisation
    # p = Path(protein.sequence, protein.length, field.coordinates)
    # p.plotFold()

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
               for k in [[1,0],[0,1]]:
                   if field.field[j + k[0]][i + k[1]] == "H":
                       points += 1
           elif field.field[j][i] == "C":
                for k in [[1,0],[0,1]]:
                    if field.field[j + k[0]][i + k[1]] == "C":
                        points += 5
    return(points)


if __name__ == '__main__':
    main()
