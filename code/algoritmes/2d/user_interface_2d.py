import time
from beam_search_2d import beam_search_2d
from greedy_2d import greedy_2d
from greedy_look_ahead_2d import greedy_look_ahead_2d
from greedy_look_ahead_beam_2d import greedy_look_ahead_beam_2d
from hillclimber_2d import hillclimber_2d

def settings_2d(sequence):

    # gives information to user
    print("You have loaded the 2-dimensional algorithms")
    time.sleep(1)

    # asks user to select an algorithm (or all of them)
    print("Please make a selection:")
    print("1. Hillclimber")
    print("2. Greedy")
    print("3. Greedy look ahead")
    print("4. Beam search")
    print("5. Beam search greedy look ahead")
    print("6. Run all algorithms")
    time.sleep(1)

    # checks if users selection is valid
    number = input("Number: ")
    while not number.isdigit() or int(number) < 1 or int(number) > 7:
        print("Please enter an integer between 1 and 5")
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
            hillclimber_2d(sequence, 8, 3)

        # runs hillclimber with settings specified by user
        else:

            # prompts user for the change length
            print("Please enter the length of the sequences that the Hillclimber will attempt to fold differently")
            time.sleep(1)
            print("Length should not be longer than the length of the protein!")
            print("Length above 10 will result in extremely long running times")
            time.sleep(1)

            # ToDO: checkt input nog niet
            change_length = input("Length: ")
            print("")

            # ToDO: checkt input nog niet
            print("Please enter the number of times the Hillclimber will loop over the entire protein")
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
        settings = input("Defaul settings for greedy look ahead? (yes or no) ")
        while settings not in yesno:
            print("Type y or n, then hit enter")
            time.sleep(1)
            settings = input("Defaul settings? ")
        print("")

        # runs hillclimber with default settings
        if settings in yes:
            print("")
            greedy_look_ahead_2d(sequence, 8, 3)

        # runs hillclimber with settings specified by user
        else:

            # prompts user for the change length
            print("Please enter the length that greedy will look ahead")
            time.sleep(1)
            print("Length should not be longer than the length of the protein!")
            print("Length above 10 will result in extremely long running times")
            time.sleep(1)

            # ToDO: checkt input nog niet
            change_length = input("Length: ")
            print("")

            # ToDO: checkt input nog niet
            print("Please enter the number of times the Hillclimber will loop over the entire protein")
            number_loops = input("Number of loops: ")

            print("")
            greedy_look_ahead_2d(sequence, int(change_length), int(number_loops))

    if number == 4 or number == 6:
        print("")
        beam_search_2d(sequence)

    if number == 5 or number == 6:
        print("")
        greedy_look_ahead_beam_2d(sequence)
