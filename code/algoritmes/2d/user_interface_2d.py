import time
from beam_search_2d import beam_search_2d
from greedy_2d import greedy_2d
from greedy_look_ahead_2d import greedy_look_ahead_2d

def settings_2d():

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
    print("5. Run all algorithms")

    # checks if users selection is valid
    number = input("Number: ")
    while not number.isdigit() or int(number) < 1 or int(number) > 6:
        print("Please enter an integer between 1 and 5")
        time.sleep(1)
        number = input("Number: ")
