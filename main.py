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
    dimension = input("Dimension: ")
    while dimension.upper() != "2D" and dimension.upper() != "3D":
        print("Input must be 2D or 3D")
        dimension = input("Dimension: ")

if __name__ == '__main__':
    main()
