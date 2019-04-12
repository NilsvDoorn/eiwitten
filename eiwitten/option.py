from itertools import product
"""Generates a list of all folding options for the protein"""
class Option(object):
    def __init__(self, length):
        self.options = list(product(["right", "left", "forward"], repeat = length - 2))
        self.count = 0

    # def automatic(self, option, protein):
    #     for i in range(len(protein)):
    #         if protein[i] == protein[i+4] == "H":
    #             if option[i] == option[i+1] == "left" or option[i] == option[i+1] == "right":
    #                 return False
    #                 self.count += 1
    #                 print(self.count)
    #                 i += 4
    #     return True
