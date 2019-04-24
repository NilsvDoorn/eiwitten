import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from field import Field






def __init__(self, protein):
    self.length = len(protein)



def getMarkerColor(self, path_dict):


def plotFold(self):
    # plot figure with size 1:1 with 100 dots per inches
    plt.figure(figsize=(1, 1), dpi=100)
    fig, ax = plt.subplots()

    x_L = -5
    x_R = 5
    y_L = -5
    y_R = 5
    ax.axis([x_L, x_R, y_L, y_R])

    list_path_data = [
        (mpath.Path.MOVETO, (0, 0)),
        (mpath.Path.LINETO, (0, -1)),

        ]

    testlist = [(1, -1), (1, 0), (2, 0), (2, -1), (3, -1), (3, -2), (2, -2)]
    testdict = {(1, -1): 'H', (1, 0): 'H', (2, 0): 'P', (2, -1): 'H', (3, -1): 'H',\
                (3, -2): 'H', (2, -2): 'H'}


    for i in testlist:
        list_path_data.extend([(mpath.Path.LINETO, i)])
    print(list_path_data)

    codes, verts = zip(*list_path_data)
    list_path = mpath.Path(verts, codes)


    # plot control points and connecting lines
    x, y = zip(*list_path.vertices)

    # color hangt af van aminozuur, placeholder = red
    # for j in testdict:
    #     if j == 'H':
    #         color = 'red'
    #     elif j == 'P':
    #         color = 'blue'
    #     elif j == 'C':
    #         color = 'yellow'

    color = 'red'
    line, = ax.plot(x, y, color='blue', linestyle='solid', marker='o', markerfacecolor=color, markersize=12)

    gridline_space = 1.0
    ax.xaxis.set_major_locator(ticker.MultipleLocator(gridline_space))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(gridline_space))
    ax.grid()

    plt.savefig("out.png")
