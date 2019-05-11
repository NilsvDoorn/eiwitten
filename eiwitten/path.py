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
    def __init__(self, protein_length, best_positions):
        self.axislength = protein_length
        self.datapoints = best_positions

    def minmax_coords(*pnts):
        mn = Point( *(min(p[i] for p in pnts) for i in range(3)) )
        mx = Point( *(max(p[i] for p in pnts) for i in range(3)) )
        return mn, mx

    # def plot3Dfold(self, proteinsequence):
    #     """This plots the 3D coordinates of the folded protein"""
    #
    #     min_x = 1000
    #     max_x = 0
    #     min_y = 1000
    #     max_y = 0
    #     min_z = 1000
    #     max_z = 0
    #     for cnd in self.datapoints:
    #         if (min_x > cnd[0]):
    #             min_x = cnd[0]
    #         if (max_x < cnd[0]):
    #             max_x = cnd[0]
    #         if (min_y > cnd[1]):
    #             min_y = cnd[1]
    #         if (max_y < cnd[1]):
    #             max_y = cnd[1]
    #         if (min_z > cnd[2]):
    #             min_z = cnd[2]
    #         if (max_z < cnd[2]):
    #             max_z = cnd[2]
    #
    #     ax.axis([(min_x - 1), (max_x + 1), (min_y - 1), (max_y + 1), (min_z - 1), (max_z - 1)]
    #
    #     list_path_data = [
    #         (mpath.Path.MOVETO, (self.datapoints[0])),
    #         ]
    #
    #     # place the code + coordinates in the list
    #     for i in self.datapoints[1:]:
    #         list_path_data.extend([(mpath.Path.LINETO, i)])
    #
    #
<<<<<<< HEAD
=======

>>>>>>> 1e8dead0ce7cbb4b6437dd6a0ed51f60b69bb6b9

    def plot3Dfold(self, proteinsequence):
        """This plots the 3D coordinates of the folded protein"""

        min_x = 1000
        max_x = 0
        min_y = 1000
        max_y = 0
        min_z = 1000
        max_z = 0
        for cnd in self.datapoints:
            if (min_x > cnd[0]):
                min_x = cnd[0]
            if (max_x < cnd[0]):
                max_x = cnd[0]
            if (min_y > cnd[1]):
                min_y = cnd[1]
            if (max_y < cnd[1]):
                max_y = cnd[1]
            if (min_z > cnd[2]):
                min_z = cnd[2]
            if (max_z < cnd[2]):
                max_z = cnd[2]

        ax.axis([(min_x - 1), (max_x + 1), (min_y - 1), (max_y + 1), (min_z - 1), (max_z - 1)])

        list_path_data = [
<<<<<<< HEAD
            (self.datapoints[0]),
=======
            (self.datapoints[0])
>>>>>>> 1e8dead0ce7cbb4b6437dd6a0ed51f60b69bb6b9
            ]

        # place the code + coordinates in the list
        for i in self.datapoints[1:]:
            list_path_data.append(i)

        # plot control points and connecting lines
        x = [t[0] for t in list_path_data]
        y = [t[1] for t in list_path_data]
        z = [t[2] for t in list_path_data]




<<<<<<< HEAD


    def plotFold(self, proteinsequence, best_fold_points):
=======
    def plotFold(self, proteinsequence, best_fold_points):

>>>>>>> 1e8dead0ce7cbb4b6437dd6a0ed51f60b69bb6b9
        """Plots the folded protein"""

        # print('this is the protein sequence: ', proteinsequence)
        # print('this is the axislength: ', self.axislength)
        # print('these are the datapoints: ', self.datapoints)

        # plot figure with size 1:1 with 100 dots per inches
        plt.figure(figsize=(6, 6), dpi=200)
        # handig voor 3D
        fig, ax = plt.subplots()

        ax.set_title('This fold has a stability of: ' + str(- best_fold_points))
<<<<<<< HEAD
=======

>>>>>>> 1e8dead0ce7cbb4b6437dd6a0ed51f60b69bb6b9

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
        list_path_data = [
            (mpath.Path.MOVETO, (self.datapoints[0])),
            ]

        # place the code + coordinates in the list
        for i in self.datapoints[1:]:
            list_path_data.extend([(mpath.Path.LINETO, i)])
        # print('this is the list_path_data')
        # print(list_path_data)

        # use the list for plotting the fold
        codes, verts = zip(*list_path_data)
        list_path = mpath.Path(verts, codes)
        # print('this is the list path')
        # print(list_path)

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

        # print('these are the h coordinates')
        # print(h_cnd_list)
        # print('these are the p coordinates')
        # print(p_cnd_list)
        # print('these are the c coordinates')
        # print(c_cnd_list)

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
