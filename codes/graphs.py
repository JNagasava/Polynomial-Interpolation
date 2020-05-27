from matplotlib import pyplot as plt

def create_graph(V, color, label):
    """
    Setup the graph informations: x values, y values, color and label name 
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
    Plot graphs 
    """
    for g in graphs:
        plt.plot(g['x'], g['y'], g['color'], label=g['label'])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()