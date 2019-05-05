import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from field import Field
from protein import Protein
from collections import namedtuple
import math

class Path(object):
    """Visualises the structure of optimal protein fold"""
<<<<<<< HEAD
    def __init__(self, protein, axislength, coordinates):
        self.protein = protein
        self.axislength = axislength
        self.path_coordinates = coordinates

    def getMarker():
        """Returns a marker with color based on the aminoacid"""
        #
        return 'red'
=======
    def __init__(self, protein_length, best_positions):
        self.axislength = protein_length
        self.datapoints = best_positions

    def minmax_coords(*pnts):
        mn = Point( *(min(p[i] for p in pnts) for i in range(3)) )
        mx = Point( *(max(p[i] for p in pnts) for i in range(3)) )
        return mn, mx
>>>>>>> c02b5b5c0aad9ed005b6e078068585f6df7efa3b


    def plotFold(self, proteinsequence):
        """Plots the folded protein"""

<<<<<<< HEAD
        print('this is the protein sequence')
        print(self.protein)
        print('this is the axislength')
        print(self.axislength)

        # plot figure with size 1:1 with 100 dots per inches
        plt.figure(figsize=(1, 1), dpi=100)
        # handig voor 3D
        fig, ax = plt.subplots()

        # use the protein length to plot graph dimensions
        x_L = self.axislength * 0.5;
        x_R = self.axislength * (-0.5);
        y_R = x_R
        y_L = x_L

        ax.axis([x_L, x_R, y_L, y_R])

        # place the folding coordinates of the field in a list
=======
        print('this is the protein sequence: ', proteinsequence)
        print('this is the axislength: ', self.axislength)
        print('these are the datapoints: ', self.datapoints)

        # plot figure with size 1:1 with 100 dots per inches
        plt.figure(figsize=(6, 6), dpi=200)
        # handig voor 3D
        fig, ax = plt.subplots()

        # find minimum x and y coordinates
        min_x = 1000
        max_x = 0
        min_y = 1000
        max_y = 0
        for cnd in self.datapoints:
            if (min_x > cnd[0]):
                min_x = cnd[0]
            if (max_x < cnd[0]):
                max_x = cnd[0]
            if (min_y > cnd[1]):
                min_y = cnd[1]
            if (max_y < cnd[1]):
                max_y = cnd[1]

        # use minimum and maximum coordinates for axis limits
        ax.axis([(min_x - 1), (max_x + 1), (min_y - 1), (max_y + 1)])

        # place the folding coordinates of the field in a list, starting cnd at protein length
>>>>>>> c02b5b5c0aad9ed005b6e078068585f6df7efa3b
        list_path_data = [
            (mpath.Path.MOVETO, (self.datapoints[0])),
            ]

<<<<<<< HEAD
        # coordinates of the aminoacids: placeholder testlist
        # testlist = [(1, -1), (1, 0), (2, 0), (2, -1), (3, -1), (3, -2), (2, -2)]
        testlist = [(1, -1), (1, 0), (2, 0), (2, -1), (3, -1), (3, -2), (2, -2)]
        testdict = {(1, -1): 'H', (1, 0): 'H', (2, 0): 'P', (2, -1): 'H', (3, -1): 'H',\
                    (3, -2): 'H', (2, -2): 'H'}

        print('these are the path_coordinates')
        print(self.path_coordinates)


=======
>>>>>>> c02b5b5c0aad9ed005b6e078068585f6df7efa3b
        # place the code + coordinates in the list
        for i in self.datapoints[1:]:
            list_path_data.extend([(mpath.Path.LINETO, i)])
<<<<<<< HEAD
        print('this is the list path data (test_list)')
=======
        print('this is the list_path_data')
>>>>>>> c02b5b5c0aad9ed005b6e078068585f6df7efa3b
        print(list_path_data)

        # use the list for plotting the fold
        codes, verts = zip(*list_path_data)
        list_path = mpath.Path(verts, codes)
        print('this is the list path (testlist)')
        print(list_path)

        # plot control points and connecting lines
        x = [t[0] for t in list_path.vertices]
        y = [t[1] for t in list_path.vertices]

        # plot sequence line
        line = ax.plot(x, y, color='blue', linestyle='solid')

        # list coordinates per aminoacid for markers
        h_cnd_list = []
        p_cnd_list = []
        c_cnd_list = []
        for aminoacid, position in zip(proteinsequence, self.datapoints):
            if aminoacid == 'H':
                h_cnd_list.append(position)
            elif aminoacid == 'P':
                p_cnd_list.append(position)
            else:
                c_cnd_list.append(position)

        print('these are the h coordinates')
        print(h_cnd_list)
        print('these are the p coordinates')
        print(p_cnd_list)
        print('these are the c coordinates')
        print(c_cnd_list)

        # self.plotMark(h_cnd_list, p_cnd_list, c_cnd_list)
        # define x, y per aminoacid
        h_x = [t[0] for t in h_cnd_list]
        h_y = [t[1] for t in h_cnd_list]

        p_x = [t[0] for t in p_cnd_list]
        p_y = [t[1] for t in p_cnd_list]

        c_x = [t[0] for t in c_cnd_list]
        c_y = [t[1] for t in c_cnd_list]

        # plot markers
        marker = ax.scatter(h_x, h_y, marker= 'o', c='red', s=50, zorder=10)
        marker = ax.scatter(p_x, p_y, marker= 'o', c='blue', s=50, zorder=10)
        marker = ax.scatter(c_x, c_y, marker= 'o', c='yellow', s=50, zorder=10)

        # # list coordinates for connection lines for h-h and c-c
        # for index in h_cnd_list:
        #     if index
        #
        #
        #
        # # plot connection lines to indicate interactions
        # connect_h = ax.plot(x, y, color='red', linestyle='--')
        # connect_c = ax.plot(x, y, color='yellow', linestyle='--')


        # plot a grid for better visualisation
        gridline_space = 1.0
        ax.xaxis.set_major_locator(ticker.MultipleLocator(gridline_space))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(gridline_space))
        ax.grid()

        plt.savefig("out.png")
