import time
import sys
sys.path.insert(0,'code/algoritmes/2d')
sys.path.insert(0,'code/algoritmes/3d')
from user_interface_2d import settings_2d
from user_interface_3d import settings_3d



def main():

    # lets user know what the program does
    print("")
    print("This program attempts to find the optimal fold for a given protein sequence in 2D or 3D")
    time.sleep(1)

    # prompts user for the protein sequence
    print("Please enter a protein sequence consisting of only H's, P's and C's (no spaces or other characters)")
    time.sleep(1)
    sequence = input("Sequence: ").upper()
    for acid in sequence:
        if acid != "H" and acid != "P" and acid != "C":
            correct = False
        else:
            correct = True
    while not correct:
        print("Input should only contain H, P and C (no spaces or other characters)")
        sequence = input("Sequence: ").upper()
        for acid in sequence:
            if acid != "H" and acid != "P" and acid != "C":
                correct = False
            else:
                correct = True

    # prompts user for the dimension that should be folded in
    print("")
    print("Would you like the fold in 2 dimensions or 3 dimensions? (enter 2D or 3D)")
    time.sleep(1)
    dimension = input("Dimension: ").upper()
    while dimension != "2D" and dimension != "3D":
        print("Input must be 2D or 3D")
        dimension = input("Dimension: ").upper()
    print("")

    if dimension == "2D":
        settings_2d()
    else:
        settings_3d()

if __name__ == '__main__':
    main()
