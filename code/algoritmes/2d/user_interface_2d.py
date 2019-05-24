import time
from beam_search_2d import beam_search_2d
from greedy_2d import greedy_2d
from greedy_look_ahead_2d import greedy_look_ahead_2d
from greedy_look_ahead_beam_2d import greedy_look_ahead_beam_2d
from hillclimber_2d import hillclimber_2d

def settings_2d(sequence):

    # gives information to user
    print("You have loaded the 2-dimensional algorithms")
    time.sleep(2)

    # asks user to select an algorithm (or all of them)
    print("Please make a selection:")
    print("1. Hillclimber")
    print("2. Greedy")
    print("3. Greedy look ahead")
    print("4. Beam search")
    print("5. Beam search greedy look ahead")
    print("6. Run all algorithms")
    number = input("Number: ")

    # checks if users selection is valid
    while not number.isdigit() or int(number) < 1 or int(number) > 7:
        print("Please enter an integer between 1 and 6")
        time.sleep(1)
        number = input("Number: ")
    number = int(number)

    # creates lists of possible valid answers and splits them in yes and no
    yesno = ["YES", "Yes", "yes", "Y", "y", "NO", "No", "no", "N", "n"]
    yes = ["YES", "Yes", "yes", "Y", "y"]

    # runs the hillclimber if it was selected by the user
    if number == 1 or number == 6:
        print("")

        # lets user choose to change settings or use default
        settings = input("Default settings for hillclimber? (yes or no) ")
        while settings not in yesno:
            print("Type y or n, then hit enter")
            time.sleep(1)
            settings = input("default settings? ")
        print("")

        # runs hillclimber with default settings
        if settings in yes:
            hillclimber_2d(sequence, 8, 3)

        # runs hillclimber with settings specified by user
        else:

            # prompts user for the change length
            print("Please enter the length of the sequences that the Hillclimber will attempt to fold differently")
            time.sleep(1)
            print("Length above 10 will result in extremely long running times")
            time.sleep(1)

            # ToDO: checkt input nog niet
            change_length = input("Length: ")
            while not change_length.isdigit() or int(change_length) > len(sequence):
                print("Please enter a positive integer that is shorter than the length of the sequence")
                time.sleep(1)
                change_length = input("Length: ")

            # ToDO: checkt input nog niet
            print("")
            print("Please enter the number of times the Hillclimber will loop over the entire protein")
            number_loops = input("Number of loops: ")
            while not number_loops.isdigit() or int(number_loops) < 1:
                print("Please enter a positive integer")
                time.sleep(1)
                number_loops = input("Number of loops: ")


            print("")
            hillclimber_2d(sequence, int(change_length), int(number_loops))


    if number == 2 or number == 6:
        print("")
        greedy_2d(sequence)

    # runs greedy look ahead if it was selected by the user
    if number == 3 or number == 6:
        print("")

        # lets user choose to change settings or use default
        settings = input("Default settings for greedy look ahead? (yes or no) ")
        while settings not in yesno:
            print("Type y or n, then hit enter")
            time.sleep(1)
            settings = input("Default settings? ")
        print("")

        # runs greedy with look ahead with default settings
        if settings in yes:
            greedy_look_ahead_2d(sequence, 8, 3)

        # runs greedy with look ahead with settings specified by user
        else:

            # prompts user for the change length
            print("Please enter the length that greedy will look ahead")
            time.sleep(1)
            print("Length above 10 will result in extremely long running times")
            time.sleep(1)
            change_length = input("Length: ")

            # checks user input
            while not change_length.isdigit() or int(change_length) > len(sequence):
                print("Please enter a positive integer that is shorter than the length of the sequence")
                time.sleep(1)
                change_length = input("Length: ")
            print("")

            # promps user for the number of loops
            print("Please enter the number of times the Hillclimber will loop over the entire protein")
            number_loops = input("Number of loops: ")

            # checks user input
            while not number_loops.isdigit() or int(number_loops) < 1:
                print("Please enter a positive integer")
                time.sleep(1)
                number_loops = input("Number of loops: ")

            print("")
            greedy_look_ahead_2d(sequence, int(change_length), int(number_loops))

    # runs beam search algorithm
    if number == 4 or number == 6:
        print("")

        # lets user choose to change settings or use default
        settings = input("Default settings for beam search? (yes or no) ")
        while settings not in yesno:
            print("Type y or n, then hit enter")
            time.sleep(1)
            settings = input("Default settings? ")
        print("")

        # runs beam search with default settings
        if settings in yes:
            beam_search_2d(sequence, 0.8, 0.25)

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

            beam_search_2d(sequence, (float(chance_one)/100), (float(chance_two)/100))

    if number == 5 or number == 6:
        print("")

        # lets user choose to change settings or use default
        settings = input("Default settings for beam search with look ahead? (yes or no) ")
        while settings not in yesno:
            print("Type y or n, then hit enter")
            time.sleep(1)
            settings = input("default settings? ")

        # runs beam search with look ahead with default settings
        if settings in yes:
            print("")
            greedy_look_ahead_beam_2d(sequence, 1, 0.8, 6)

        # runs beam search with settings specified by user
        else:

            # prompts user for the percentage of bad options that will get pruned
            print("Please enter the chance that beam search with look ahead will prune bad options (0-100)")
            time.sleep(1)
            print("Percentage below 70 will result in extremely long running times")
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
            print("Percentage below 20 will result in extremely long running times")
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
            print("Length above 9 will result in extremely long running times")
            time.sleep(1)
            steps = input("Length: ")

            # checks user input
            while not steps.isdigit() or int(steps) > len(sequence):
                print("Please enter a positive integer that is shorter than the length of the sequence")
                time.sleep(1)
                steps = input("Length: ")
            print("")

            greedy_look_ahead_beam_2d(sequence, float(chance_one/100), float(chance_two/100), int(steps))
