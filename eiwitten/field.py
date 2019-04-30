class Field(object):
    """Initialises field for protein to fold in"""
    def __init__(self, length, sequence):
        self.dimension = (length * 2)
        self.field = [["_"] * self.dimension for i in range(self.dimension)]
