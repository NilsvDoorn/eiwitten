import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from field import Field
from protein import Protein
import math

class Path(object):
    """Visualises the structure of optimal protein fold"""
    def __init__(self, protein, protein_length, coordinates):
        self.protein = protein
        self.axislength = len(self.protein)
        self.datapoints = coordinates

    def markerColor(self):
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
        # handig voor 3D
        fig, ax = plt.subplots()

        # use the protein length to plot graph dimensions
        x_L = math.ceil(self.axislength * 2);
        x_R = math.ceil(self.axislength * 2);
        y_L = x_L;
        y_R = x_R;

        ax.axis([x_L, x_R, y_L, y_R])

        # place the folding coordinates of the field in a list, starting cnd at protein length
        list_path_data = [
            (mpath.Path.MOVETO, (self.axislength, self.axislength)),
            (mpath.Path.LINETO, (self.axislength, self.axislength - 1)),

            ]

        # coordinates of the aminoacids: placeholder testlist
        testlist = [(1, -1), (1, 0), (2, 0), (2, -1), (3, -1), (3, -2), (2, -2)]
        testdict = {(1, -1): 'H', (1, 0): 'H', (2, 0): 'P', (2, -1): 'H', (3, -1): 'H',\
                    (3, -2): 'H', (2, -2): 'H'}

        # place the code + coordinates in the list
        for i in self.datapoints:
            list_path_data.extend([(mpath.Path.LINETO, i)])
        print(list_path_data)

        # use the list for plotting the fold
        codes, verts = zip(*list_path_data)
        list_path = mpath.Path(verts, codes)

        # plot control points and connecting lines
        x = [t[0] for t in list_path.vertices]
        y = [t[1] for t in list_path.vertices]


        # plot line and markers
        line = ax.plot(x, y, color='blue', linestyle='solid')
        # marker, = ax.scatter(x, y, marker= 'o', markerfacecolor=self.getMarker(), markersize=12)

        marker = ax.scatter(x, y, marker= 'o', c='red', s=12)

        # plot a grid for better visualisation
        gridline_space = 1.0
        ax.xaxis.set_major_locator(ticker.MultipleLocator(gridline_space))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(gridline_space))
        ax.grid()

        plt.savefig("out.png")
