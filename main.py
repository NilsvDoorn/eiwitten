import sys
sys.path.insert(0,'code/algoritmes/2d')
sys.path.insert(0,'code/algoritmes/3d')
sys.path.insert(0,'code/classes')
from user_interface_2d import settings_2d
from user_interface_3d import settings_3d
import time

def main():

    # lets user know what the program does
    print("")
    print("This program attempts to find the optimal fold for a given protein sequence in 2D or 3D")
    time.sleep(1)

    # prompts user for the protein sequence
    print("Please enter a protein sequence consisting of only H's, P's and C's (no spaces or other characters)")
    time.sleep(1)
    sequence = input("Sequence: ").upper()
    correct = True
    for acid in sequence:
        if acid != "H" and acid != "P" and acid != "C":
            correct = False

    # checks if user input is correct, prompts again if not
    while not correct:
        correct = True
        print("Input should only contain H, P and C (no spaces or other characters, example: HHHPPPCCC)")
        sequence = input("Sequence: ").upper()
        for acid in sequence:
            if acid != "H" and acid != "P" and acid != "C":
                correct = False

    # prompts user for the dimension that should be folded in
    print("")
    print("Would you like the fold in 2 dimensions or 3 dimensions? (enter 2D or 3D)")
    time.sleep(1)
    valid_dimensions = ["2", "2d", "2D", "3", "3d", "3D"]
    two_dimensional = ["2", "2d", "2D"]
    dimension = input("Dimension: ").upper()

    # checks if user input is correct, prompts again if not
    while dimension not in valid_dimensions:
        print("Input must be 2D or 3D")
        dimension = input("Dimension: ").upper()

    print("")

    # moves to the proper dimensional folder
    if dimension in two_dimensional:
        settings_2d(sequence)
    else:
        settings_3d(sequence)

if __name__ == '__main__':
    main()
