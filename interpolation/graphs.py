"""
Create and Plot Graphs
"""

from matplotlib import pyplot as plt

def create_graph(V, color, label):
    """
    Setup the graph informations: x values, y values, color and label name.

    Parameters
    ----------
        V : dict
            V contains X and Y values.
        color : str
            color name.
        label : str
            label name

    Returns
    -------
        dict : 
            Returns a dict = {'x': X, 'y': Y, 'color': color, 'label': label}
    """    
    x, y = list(V.keys())
    return {
        'x': V[x],
        'y': V[y],
        'color': color,
        'label': label
    }

def plot_graph(graphs, title=None, xlabel='x', ylabel='y'):
    """
    Plot graphs using matplot libray

    Paramaters
    ----------
        graphs : list
            List of created graphs
        title : str
            title of graph
        xlabel : str
            name of x axis
        ylabel : str
            name of y axis
    """
    for g in graphs:
        plt.plot(g['x'], g['y'], g['color'], label=g['label'])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()