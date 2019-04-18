from itertools import product
"""Generates a list of all folding options for the protein"""
class Option(object):
    def __init__(self, length):
        self.options = ["right", "left", "forward"]

    def cluster(self, sequence, option):
        length_sequence = len(sequence) - 3
        i = 0
        while i < length_sequence:
            if sequence[i] == sequence[i+3] == "H":
                if option[i] != option[i+1] or option[i] == "forward":
                    return False
                else:
                    i += 2
            i += 1
        return True
