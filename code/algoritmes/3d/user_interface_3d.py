from beam_search import beam_search
from greedy import greedy
from greedy_look_ahead import greedy_look_ahead
from greedy_look_ahead_beam import greedy_look_ahead_beam
from multiple_step_breadth_first import multiple_step_breadth_first
import time

def settings_3d(sequence):
    print("You have loaded the 3-dimensional algorithms")
    time.sleep(2)

    # asks user to select an algorithm (or all of them)
    print("Please make a selection:")
    print("1. Multiple step breadth first")
    print("2. Greedy")
    print("3. Greedy with look ahead")
    print("4. Beam search")
    print("5. Beam search with look ahead")
    print("6. Run all algorithms")

    # checks if users selection is valid
    number = input("Number: ")
    while not number.isdigit() or int(number) < 1 or int(number) > 7:
        print("Please enter an integer between 1 and 6")
        time.sleep(1)
        number = input("Number: ")
    number = int(number)

    # creates lists of possible valid answers and splits them in yes and no
    yesno = ["YES", "Yes", "yes", "Y", "y", "NO", "No", "no", "N", "n"]
    yes = ["YES", "Yes", "yes", "Y", "y"]

    # runs multiple step breadth first if it was selected by the user
    if number == 1 or number == 6:
        print("")

        # lets user choose to change settings or use default
        print("Default settings for multiple step breadth first? (yes or no) ")
        print("Default: Length of change = 6, Number of loops = 3")
        settings = input("Default settings? ")

        # checks user input
        while settings not in yesno:
            print("Type y or n, then hit enter")
            time.sleep(1)
            settings = input("default settings? ")
        print("")

        # runs multiple step breadth first with default settings
        if settings in yes:
            multiple_step_breadth_first(sequence, 6, 3)

        # runs multiple step breadth first with settings specified by user
        else:

            # prompts user for the change length
            print("Please enter the length of the sequences that the multiple step breadth first will attempt to fold differently")
            time.sleep(1)
            print("Length above 8 will result in extremely long running times")
            time.sleep(1)
            change_length = input("Length: ")

            # checks user input
            while not change_length.isdigit() or int(change_length) > len(sequence):
                print("Please enter a positive integer that is shorter than the length of the sequence")
                time.sleep(1)
                change_length = input("Length: ")
            print("")

            # prompts user for the number of loops
            print("Please enter the number of times the multiple step breadth first will loop over the entire protein")
            number_loops = input("Number of loops: ")

            # checks user input
            while not number_loops.isdigit() or int(number_loops) < 1:
                print("Please enter a positive integer")
                time.sleep(1)
                number_loops = input("Number of loops: ")
            print("")

            # runs multiple step breadth first with user settings
            multiple_step_breadth_first(sequence, int(change_length), int(number_loops))

    # runs greedy if it was selected by the user
    if number == 2 or number == 6:
        print("")
        greedy(sequence)

    # runs the greedy with look ahead if it was selected by the user
    if number == 3 or number == 6:
        print("")

        # lets user choose to change settings or use default
        print("Default settings for multiple step breadth first? (yes or no) ")
        print("Default: Number of steps = 6s, Number of loops = 3")
        settings = input("Default settings? ")

        # checks user input
        while settings not in yesno:
            print("Type y or n, then hit enter")
            time.sleep(1)
            settings = input("Default settings? ")
        print("")

        # runs greedy with look ahead with default settings
        if settings in yes:
            greedy_look_ahead(sequence, 6, 3)

        # runs greedy with look ahead with settings specified by user
        else:

            # prompts user for the change length
            print("Please enter the number of steps")
            time.sleep(1)
            print("More than 8 steps will result in extremely long running times")
            time.sleep(1)
            change_length = input("Steps: ")

            # checks user input
            while not change_length.isdigit() or int(change_length) > len(sequence):
                print("Please enter a positive integer that is shorter than the length of the sequence")
                time.sleep(1)
                change_length = input("Steps: ")
            print("")

            # promps user for the number of loops
            print("Please enter the number of times the greedy with look ahead will loop over the entire protein")
            number_loops = input("Number of loops: ")

            # checks user input
            while not number_loops.isdigit() or int(number_loops) < 1:
                print("Please enter a positive integer")
                time.sleep(1)
                number_loops = input("Number of loops: ")
            print("")

            # runs greedy with look ahead with user settings
            greedy_look_ahead(sequence, int(change_length), int(number_loops))

    # runs beam search if it was selected by the user
    if number == 4 or number == 6:
        print("")

        # lets user choose to change settings or use default
        print("Default settings for beam search? (yes or no) ")
        print("Default: Chance to prune good options = 0.25, Chance to prune bad options = 0.8")
        settings = input("Default settings? ")

        # checks user input
        while settings not in yesno:
            print("Type y or n, then hit enter")
            time.sleep(1)
            settings = input("Default settings? ")
        print("")

        # runs beam search with default settings
        if settings in yes:
            beam_search(sequence, 0.8, 0.25)

        # runs beam search with settings specified by user
        else:

            # prompts user for the percentage of good options that will get pruned
            print("Please enter the chance that beam search will prune bad options (0-100)")
            time.sleep(1)
            print("Percentage below 70 will result in extremely long running times")
            chance_one = input("Chance: ")

            # checks user input
            while not chance_one.isdigit() or int(chance_one) > 100:
                print("Please enter an integer between 0 and 100")
                time.sleep(1)
                chance_one = input("Chance: ")
            print("")

            # prompts user for the percentage of good options that will get pruned
            print("Please enter the chance that beam search will prune good options (0-100)")
            time.sleep(1)
            print("Percentage below 20 will result in extremely long running times")
            time.sleep(1)
            chance_two = input("Chance: ")

            # checks user input
            while not chance_two.isdigit() or int(chance_two) > 100:
                print("Please enter an integer between 0 and 100")
                time.sleep(1)
                chance_two = input("Chance: ")
            print("")

            # runs beam search with user settings
            beam_search(sequence, (float(chance_one)/100), (float(chance_two)/100))

    # runs bream search with look ahead if it was selected by the user
    if number == 5 or number == 6:
        print("")

        # lets user choose to change settings or use default
        print("Default settings for beam search with look ahead? (yes or no) ")
        print("Default: Chance to prune good options = 100, Chance to prune bad options = 100, Steps = 5")
        settings = input("Default settings? ")

        # checks user input
        while settings not in yesno:
            print("Type y or n, then hit enter")
            time.sleep(1)
            settings = input("default settings? ")
        print("")

        # runs beam search with look ahead with default settings
        if settings in yes:
            greedy_look_ahead_beam(sequence, 1, 1, 5)

        # runs beam search with settings specified by user
        else:

            # prompts user for the percentage of bad options that will get pruned
            print("Please enter the chance that beam search with look ahead will prune bad options (0-100)")
            time.sleep(1)
            print("Percentage below 95 will result in extremely long running times")
            time.sleep(1)
            chance_one = input("Chance: ")

            # checks user input
            while not chance_one.isdigit() or int(chance_one) > 100:
                print("Please enter an integer between 0 and 100")
                time.sleep(1)
                chance_one = input("Chance: ")
            print("")

            # prompts user for the percentage of good options that will get pruned
            print("Please enter the chance that beam search with look ahead will prune good options (0-100)")
            time.sleep(1)
            print("Percentage below 80 will result in extremely long running times")
            time.sleep(1)
            chance_two = input("Chance: ")

            # checks user input
            while not chance_two.isdigit() or int(chance_two) > 100:
                print("Please enter an integer between 0 and 100")
                time.sleep(1)
                chance_two = input("Chance: ")
            print("")

            # prompts user for the change length
            print("Please enter the length that beam search will look ahead")
            time.sleep(1)
            print("Length above 6 will result in extremely long running times")
            time.sleep(1)
            steps = input("Length: ")

            # checks user input
            while not steps.isdigit() or int(steps) > len(sequence):
                print("Please enter a positive integer that is shorter than the length of the sequence")
                time.sleep(1)
                steps = input("Length: ")
            print("")

            # runs beam search with look ahead with user settings
            greedy_look_ahead_beam(sequence, (float(chance_one)/100), (float(chance_two)/100), int(steps))
