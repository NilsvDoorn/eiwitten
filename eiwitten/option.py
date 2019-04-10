from itertools import product
"""Generates a list of all folding options for the protein"""
class Option(object):
    def __init__(self, length):
        self.options = list(product(["right", "left", "up", "down"], repeat = length - 2))
