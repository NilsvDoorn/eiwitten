from itertools import product
from math import ceil
"""Generates a list of all folding options for the protein"""
class Option(object):
    def __init__(self):
        self.options = ["right", "forward", "left", "up", "down", "back"]
        self.options_2D = ["right", "forward", "left"]

    def mirror(self, route):
        for option in route:
            if option == 'right':
                return False
            elif option == 'left' or option == "up" or option == "down":
                return True
        return True
