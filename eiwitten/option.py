from itertools import product

class Option(object):
    def __init__(self, length):
        self.options = ["right", "forward", "left"]

    def mirror(self, route):
        for option in route:
            if option == 'right':
                return False
            elif option == 'left':
                return True
        return True

    def PPP(self, eiwit, route):
        if eiwit[len(route) - 1] == eiwit[len(route)] == eiwit[len(route) + 1] == 'P' and route[-1] == 'forward':
            return True
        else:
            return False


    # finds all x,y amino positions of current option
    def amino_positions(option):
        positions = []
        x, y = 10, 10
        positions.append(tuple((x, y + 1)))
        positions.append(tuple((x, y)))
        direction = "d"
        for move in option:
            if direction == "d":
                if move == "right":
                    x = x - 1
                    direction = "l"
                elif move == "left":
                    x = x + 1
                    direction = "r"
                elif move == "forward":
                    y = y - 1
            elif direction == "r":
                if move == "right":
                    y = y - 1
                    direction = "d"
                elif move == "left":
                    y = y + 1
                    direction = "u"
                elif move == "forward":
                    x = x + 1
            elif direction == "l":
                if move == "right":
                    y = y + 1
                    direction = "u"
                elif move == "left":
                    y = y - 1
                    direction = "d"
                elif move == "forward":
                    x = x - 1
            elif direction == "u":
                if move == "right":
                    x = x + 1
                    direction = "r"
                elif move == "left":
                    x = x - 1
                    direction = "l"
                elif move == "forward":
                    y = y + 1
            positions.append(tuple((x, y)))
        return positions

    # determines if current fold option results in bumps
    def viable_option(option):
        number = 1
        for position in option:
            for i in range(len(option) - number):
                if option[i + number] == position:
                    return False
            number += 1
        return True

    def fold_points(positions, sequence):
        points = 0
        HHHH = []
        CCCC = []
        for position, acid in zip(positions, sequence):
            if acid == "H":
                HHHH.append(position)
            elif acid == "C":
                CCCC.append(position)
        for i in range(len(HHHH)):
            if (HHHH[i][0] - 1, HHHH[i][1]) in (HHHH or CCCC):
                points += 1
            if (HHHH[i][0], HHHH[i][1] - 1) in (HHHH or CCCC):
                points += 1
        for i in range(len(CCCC)):
            if (CCCC[i][0] - 1, CCCC[i][1]) in CCCC:
                points += 5
            elif (CCCC[i][0] - 1, CCCC[i][1]) in HHHH:
                points += 1
            if (CCCC[i][0], CCCC[i][1] - 1) in CCCC:
                points += 5
            elif (CCCC[i][0], CCCC[i][1] - 1) in HHHH:
                points += 1
        return points
