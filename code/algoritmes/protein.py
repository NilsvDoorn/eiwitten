"""Initialises protein class which remembers the sequence, length, """
"""errorpoints and lower bound of the selected protein             """
class Protein(object):
    def __init__(self, protein):
        self.sequence = protein
        self.length = len(protein)
        self.errorpoint = self.errorcalculator()

    """Determines points that are rewarded for aminoacids that are next"""
    """to eachother in the sequence                                    """
    def errorcalculator(self):
        points = 0
        point_list = [0]
        for i in range(self.length - 1):
            if self.sequence[i] == self.sequence[i + 1] == "H":
                points += 1
            elif self.sequence[i] == self.sequence[i + 1] == "C":
                points += 5
            elif self.sequence[i] == "C" and self.sequence[i + 1] == "H":
                points += 1
            elif self.sequence[i] == "H" and self.sequence[i + 1] == "C":
                points += 1
            point_list.append(points)
        return(point_list)
