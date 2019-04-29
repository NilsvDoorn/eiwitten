import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from field import Field
from protein import Protein
import math

class Path(object):
    """Visualises the structure of optimal protein fold"""
    def __init__(self, protein_length, best_positions):
        self.axislength = protein_length
        self.datapoints = best_positions


    def plotFold(self, proteinsequence):
        """Plots the folded protein"""

        print('this is the protein sequence')
        print(proteinsequence)
        print('this is the axislength')
        print(self.axislength)
        print('these are the datapoints')
        print(self.datapoints)

        # plot figure with size 1:1 with 100 dots per inches
        plt.figure(figsize=(1, 1), dpi=100)
        # handig voor 3D
        fig, ax = plt.subplots()

        # use the protein length to plot graph dimensions
        x_L = 0
        x_R = self.axislength
        y_L = x_L
        y_R = x_R

        ax.axis([x_L, x_R, y_L, y_R])

        # place the folding coordinates of the field in a list, starting cnd at protein length
        list_path_data = [
            (mpath.Path.MOVETO, (self.datapoints[0])),
            ]

        # place the code + coordinates in the list
        for i in self.datapoints[1:]:
            list_path_data.extend([(mpath.Path.LINETO, i)])
        print('this is the list_path_data')
        print(list_path_data)

        # use the list for plotting the fold
        codes, verts = zip(*list_path_data)
        list_path = mpath.Path(verts, codes)

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
