import matplotlib.path as mpath
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from protein import Protein
import math
from mpl_toolkits.mplot3d import axes3d, Axes3D

class Path(object):
    """Visualises the structure of optimal protein fold"""
    def __init__(self, protein_length, best_positions):
        self.axislength = protein_length
        self.datapoints = best_positions

    # def minmax_coords(*pnts):
    #     mn = Point( *(min(p[i] for p in pnts) for i in range(3)) )
    #     mx = Point( *(max(p[i] for p in pnts) for i in range(3)) )
    #     return mn, mx

    def plot3Dfold(self, proteinsequence, best_fold_points):
        """This plots the 3D coordinates of the folded protein"""

        # initialise figure
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.set_title('This fold has a stability of: ' + str(- best_fold_points))


        # create list with path coordinates
        list_3D_path = self.datapoints


        # plot control points and connecting lines
        x = [t[0] for t in list_3D_path]
        y = [t[1] for t in list_3D_path]
        z = [t[2] for t in list_3D_path]


        # plot sequence line
        line_3D = ax.plot(x, y, z, color='black', linestyle='solid')


        # list coordinates per aminoacid for markers
        h_3D_cnd_list = []
        p_3D_cnd_list = []
        c_3D_cnd_list = []
        for aminoacid, position in zip(proteinsequence, self.datapoints):
            if aminoacid == 'H':
                h_3D_cnd_list.append(position)
            elif aminoacid == 'P':
                p_3D_cnd_list.append(position)
            else:
                c_3D_cnd_list.append(position)

        # print('these are the h coordinates')
        # print(h_cnd_list)
        # print('these are the p coordinates')
        # print(p_cnd_list)
        # print('these are the c coordinates')
        # print(c_cnd_list)

        # define x, y per aminoacid
        h_x_3D = [t[0] for t in h_3D_cnd_list]
        h_y_3D = [t[1] for t in h_3D_cnd_list]
        h_z_3D = [t[2] for t in h_3D_cnd_list]

        p_x_3D = [t[0] for t in p_3D_cnd_list]
        p_y_3D = [t[1] for t in p_3D_cnd_list]
        p_z_3D = [t[2] for t in p_3D_cnd_list]

        c_x_3D = [t[0] for t in c_3D_cnd_list]
        c_y_3D = [t[1] for t in c_3D_cnd_list]
        c_z_3D = [t[2] for t in c_3D_cnd_list]

        # plot markers
        ax.scatter(h_x_3D, h_y_3D, h_z_3D, marker= 'o', c='red', s=100, label='H', zorder=10)
        ax.scatter(p_x_3D, p_y_3D, p_z_3D, marker= 'o', c='blue', s=100, label='P', zorder=10)

        if len(c_3D_cnd_list) is not 0:
            ax.scatter(c_x_3D, c_y_3D, c_z_3D, marker= 'o', c='yellow', s=100, label='C', zorder=10)


        # make the fold determine axis length
        min_x_3D = 1000
        max_x_3D = 0
        min_y_3D = 1000
        max_y_3D = 0
        min_z_3D = 1000
        max_z_3D = 0
        for cnd in self.datapoints:
            if (min_x_3D > cnd[0]):
                min_x_3D = cnd[0]
            if (max_x_3D < cnd[0]):
                max_x_3D = cnd[0]
            if (min_y_3D > cnd[1]):
                min_y_3D = cnd[1]
            if (max_y_3D < cnd[1]):
                max_y_3D = cnd[1]
            if (min_z_3D > cnd[2]):
                min_z_3D = cnd[2]
            if (max_z_3D < cnd[2]):
                max_z_3D = cnd[2]

        # Make legend, set axes limits and labels
        ax.legend()
        ax.set_xlim((min_x_3D - 1), (max_x_3D + 1))
        ax.set_ylim((min_y_3D - 1), (max_y_3D + 1))
        ax.set_zlim((min_z_3D - 1), (max_z_3D + 1))
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')

        # ax.axis([(min_x_3D - 1), (max_x_3D + 1), (min_y_3D - 1), (max_y_3D + 1), (min_z_3D - 1), (max_z_3D + 1)])

        # disable axis ticks
        # ax.tick_params(axis= 'both', which= 'both', bottom= False, top= False, left= False, right= False)
        ax.set_xticks(np.array([]))
        ax.set_yticks(np.array([]))
        ax.set_zticks(np.array([]))

        # ax.set_axis_off()

        plt.savefig("3D_out.png")

        plt.show()






    def plotFold(self, proteinsequence, best_fold_points):

        """Plots the folded protein"""

        # plot figure with size 1:1 with 100 dots per inches
        plt.figure(figsize=(6, 6), dpi=200)
        # handig voor 3D
        fig, ax = plt.subplots()

        ax.set_title('This fold has a stability of: ' + str(- best_fold_points))


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

        # use the list for plotting the fold
        codes, verts = zip(*list_path_data)
        list_path = mpath.Path(verts, codes)

        # plot control points and connecting lines
        x = [t[0] for t in list_path.vertices]
        y = [t[1] for t in list_path.vertices]

        # plot sequence line
        line = ax.plot(x, y, color='black', linestyle='solid')

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

        # define x, y per aminoacid
        h_x = [t[0] for t in h_cnd_list]
        h_y = [t[1] for t in h_cnd_list]

        p_x = [t[0] for t in p_cnd_list]
        p_y = [t[1] for t in p_cnd_list]

        c_x = [t[0] for t in c_cnd_list]
        c_y = [t[1] for t in c_cnd_list]

        # plot markers
        marker = ax.scatter(h_x, h_y, marker= 'o', c='red', s=100, zorder=10)
        marker = ax.scatter(p_x, p_y, marker= 'o', c='blue', s=100, zorder=10)
        marker = ax.scatter(c_x, c_y, marker= 'o', c='yellow', s=100, zorder=10)

        # plot a grid for better visualisation
        gridline_space = 1.0
        ax.xaxis.set_major_locator(ticker.MultipleLocator(gridline_space))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(gridline_space))
        ax.grid()

        # disable axis ticks
        # ax.tick_params(axis= 'both', which= 'both', bottom= False, top= False)
        ax.set_xticks(np.array([]))
        ax.set_yticks(np.array([]))

        # plot a grid for better visualisation
        gridline_space = 1.0
        ax.grid()


        plt.savefig("2D_out.png")