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
    time.sleep(1)
    print("1. Hillclimber")
    print("2. Greedy")
    print("3. Greedy look ahead")
    print("4. Beam search")
    print("5. Beam search greedy look ahead")
    print("6. Run all algorithms")

    # checks if users selection is valid
    number = input("Number: ")
    while not number.isdigit() or int(number) < 1 or int(number) > 7:
        print("Please enter an integer between 1 and 5")
        time.sleep(1)
        number = input("Number: ")
    number = int(number)

    if number == 1 or number == 6:
        hillclimber_2d(sequence)

    if number == 2 or number == 6:
        greedy_2d(sequence)

    if number == 3 or number == 6:
        greedy_look_ahead_2d(sequence)

    if number == 4 or number == 6:
        beam_search_2d(sequence)

    if number == 5 or number == 6:
        greedy_look_ahead_beam_2d(sequence)
