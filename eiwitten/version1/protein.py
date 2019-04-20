class Protein(object):
    def __init__(self, protein):
        self.sequence = protein
        self.length = len(protein)
        self.errorpoint = self.errorcalculator()

    def errorcalculator(self):
        points = 0
        for i in range(self.length - 1):
                if self.sequence[i] == self.sequence[i + 1] == "H":
                    points += 1
                elif self.sequence[i] == self.sequence[i + 1] == "C":
                    points += 5
        return(points)
