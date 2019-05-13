"""Initialises protein class which remembers the sequence, length, """
"""errorpoints and lower bound of the selected protein             """
class Protein(object):
    def __init__(self, protein):
        self.sequence = protein
        self.length = len(protein)
        self.errorpoint = self.errorcalculator()
        self.lower_bound = self.minimum()

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

    """Determines minimum number of points for each point in the sequence"""
    def minimum(self):
        points = 0
        point_list = []
        for i in range(self.length):
            if self.sequence[i] == "H":
                points += 1
            elif self.sequence[i] == "C":
                points += 5
            point_list.append(points // 4)
        return(point_list)
