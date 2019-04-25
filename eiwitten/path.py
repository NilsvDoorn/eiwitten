import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from field import Field
from protein import Protein

class Path(object):
    """Visualises the structure of optimal protein fold"""
    def __init__(self, protein, axislength, coordinates):
        self.protein = protein
        self.axislength = axislength
        self.datapoints = coordinates

    def getMarker():
        """Returns a marker with color based on the aminoacid"""
        return 'red'

        # self.path_dict = {}

    def plotFold(self):

        print('this is the protein sequence')
        print(self.protein)
        print('this is the axislength')
        print(self.axislength)
        # plot figure with size 1:1 with 100 dots per inches
        plt.figure(figsize=(1, 1), dpi=100)
        fig, ax = plt.subplots()

        # use the protein length to plot graph dimensions
        x_L = self.axislength * -0.5
        x_R = self.axislength * 0.5
        y_L = self.axislength * -0.5
        y_R = self.axislength * 0.5
        ax.axis([x_L, x_R, y_L, y_R])

        # place the folding coordinates of the field in a list
        list_path_data = [
            (mpath.Path.MOVETO, (0, 0)),
            (mpath.Path.LINETO, (0, -1)),

            ]

        # coordinates of the aminoacids: placeholder testlist
        testlist = [(1, -1), (1, 0), (2, 0), (2, -1), (3, -1), (3, -2), (2, -2)]
        testdict = {(1, -1): 'H', (1, 0): 'H', (2, 0): 'P', (2, -1): 'H', (3, -1): 'H',\
                    (3, -2): 'H', (2, -2): 'H'}

        # place the code + coordinates in the list
        for i in testlist:
            list_path_data.extend([(mpath.Path.LINETO, i)])
        print(list_path_data)

        # use the list for plotting the fold
        codes, verts = zip(*list_path_data)
        list_path = mpath.Path(verts, codes)

        # plot control points and connecting lines
        x, y = zip(*list_path.vertices)

        # plot line and markers
        line, = ax.plot(x, y, color='blue', linestyle='solid')
        marker, = ax.plot(x, y, marker= 'o', markerfacecolor=getMarker(), markersize=12)

        # import itertools
        # marker = itertools.cycle((',', '+', '.', 'o', '*'))
        # for n in y:
        #     plt.plot(x,n, marker = next(marker), linestyle='')

        # plot a grid for better visualisation
        gridline_space = 1.0
        ax.xaxis.set_major_locator(ticker.MultipleLocator(gridline_space))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(gridline_space))
        ax.grid()

        plt.savefig("out.png")
        
