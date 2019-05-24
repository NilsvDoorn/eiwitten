from beam_search import beam_search
from greedy import greedy
from greedy_look_ahead import greedy_look_ahead
from greedy_look_ahead_beam import greedy_look_ahead_beam
from hillclimber import hillclimber
import time

def settings_3d(sequence):
    print("You have loaded the 3-dimensional algorithms")
    time.sleep(2)

    # asks user to select an algorithm (or all of them)
    print("Please make a selection:")
    print("1. Hillclimber")
    print("2. Greedy")
    print("3. Greedy look ahead")
    print("4. Beam search")
    print("5. Beam search greedy look ahead")
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

    # runs the hillclimber if it was selected by the user
    if number == 1 or number == 6:
        print("")

        # lets user choose to change settings or use default
        settings = input("Defaul settings for hillclimber? (yes or no) ")
        while settings not in yesno:
            print("Type y or n, then hit enter")
            time.sleep(1)
            settings = input("Defaul settings? ")
        print("")

        # runs hillclimber with default settings
        if settings in yes:
            print("")
            hillclimber(sequence, 6, 3)

        # runs hillclimber with settings specified by user
        else:

            # prompts user for the change length
            print("Please enter the length of the sequences that the Hillclimber will attempt to fold differently")
            time.sleep(1)
            print("Length should not be longer than the length of the protein!")
            print("Length above 8 will result in extremely long running times")
            time.sleep(1)

            # ToDO: checkt input nog niet
            change_length = input("Length: ")
            print("")

            # ToDO: checkt input nog niet
            print("Please enter the number of times the Hillclimber will loop over the entire protein")
            number_loops = input("Number of loops: ")

            print("")
            hillclimber(sequence, int(change_length), int(number_loops))


    if number == 2 or number == 6:
        print("")
        greedy(sequence)

    # runs greedy look ahead if it was selected by the user
    if number == 3 or number == 6:
        print("")

        # lets user choose to change settings or use default
        settings = input("Defaul settings for greedy look ahead? (yes or no) ")
        while settings not in yesno:
            print("Type y or n, then hit enter")
            time.sleep(1)
            settings = input("Defaul settings? ")
        print("")

        # runs greedy with look ahead with default settings
        if settings in yes:
            print("")
            greedy_look_ahead(sequence, 6, 3)

        # runs greedy with look ahead with settings specified by user
        else:

            # prompts user for the change length
            print("Please enter the length that greedy will look ahead")
            time.sleep(1)
            print("Length should not be longer than the length of the protein!")
            print("Length above 8 will result in extremely long running times")
            time.sleep(1)

            # ToDO: checkt input nog niet
            change_length = input("Length: ")
            print("")

            # ToDO: checkt input nog niet
            print("Please enter the number of times the Hillclimber will loop over the entire protein")
            number_loops = input("Number of loops: ")

            print("")
            greedy_look_ahead(sequence, int(change_length), int(number_loops))

    if number == 4 or number == 6:
        print("")

        # lets user choose to change settings or use default
        settings = input("Default settings for beam search? (yes or no) ")
        while settings not in yesno:
            print("Type y or n, then hit enter")
            time.sleep(1)
            settings = input("Defaul settings? ")

        # runs beam search with default settings
        if settings in yes:
            print("")
            beam_search(sequence, 0.8, 0.25)

        # runs beam search with settings specified by user
        else:

            # prompts user for the percentage of bad options that will get pruned
            print("Please enter the chance that beam search will keep good options (x.xx)")
            time.sleep(1)
            print("Percentage below ?? will result in extremely long running times")
            time.sleep(1)

            # ToDO: checkt input nog niet
            chance_one = input("Chance: ")
            print("")

            # prompts user for the percentage of bad options that will get pruned
            print("Please enter the chance that beam search will keep bad options (x.xx)")
            time.sleep(1)
            print("Percentage below ?? will result in extremely long running times")
            time.sleep(1)

            # ToDO: checkt input nog niet
            chance_two = input("Chance: ")

            print("")
            beam_search(sequence, float(chance_one), float(chance_two))

    if number == 5 or number == 6:
        print("")

        # lets user choose to change settings or use default
        settings = input("Default settings for beam search with look ahead? (yes or no) ")
        while settings not in yesno:
            print("Type y or n, then hit enter")
            time.sleep(1)
            settings = input("Defaul settings? ")

        # runs beam search with look ahead with default settings
        if settings in yes:
            print("")
            greedy_look_ahead_beam(sequence, 1, 0.8, 6)

        # runs beam search with settings specified by user
        else:

            # prompts user for the percentage of bad options that will get pruned
            print("Please enter the chance that beam search with look ahead will keep good options (x.xx)")
            time.sleep(1)
            print("Percentage below ?? will result in extremely long running times")
            time.sleep(1)

            # ToDO: checkt input nog niet
            chance_one = input("Chance: ")
            print("")

            # prompts user for the percentage of bad options that will get pruned
            print("Please enter the chance that beam search with look ahead will keep bad options (x.xx)")
            time.sleep(1)
            print("Percentage below ?? will result in extremely long running times")
            time.sleep(1)

            # ToDO: checkt input nog niet
            chance_two = input("Chance: ")
            print("")

            # prompts user for the step length
            print("Please enter the length that beam search will look ahead")
            time.sleep(1)
            print("Length should not be longer than the length of the protein!")
            print("Length above  5 will result in extremely long running times")
            time.sleep(1)

            # ToDO: checkt input nog niet
            steps = input("Length: ")

            print("")
            greedy_look_ahead_beam(sequence, float(chance_one), float(chance_two), int(steps))
