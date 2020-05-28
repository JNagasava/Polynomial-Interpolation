"""
Handles csv files (write and read)
"""

import csv

def create_csv(X, Y, xlabel, ylabel, name):
    """
    Create csv file from X and Y values.

    Parameters
    ----------
        X : list
            list of x values
        Y : list
            list of y values
        xlabel : str
            name of x axis
        xlabel : str
            name of y axis
        name : str
            name of csv file
    
    Notes
    -----
    The name of `csv file` `doesn't have` to end with `.csv` 
    """
    with open(f'data/{name}.csv', 'w') as f :
        writer = csv.DictWriter(f, fieldnames=[f'{xlabel}', f'{ylabel}'])
        writer.writeheader()
        writer.writerows([{f'{xlabel}': pair[0], f'{ylabel}': pair[1]} for pair in zip(X, Y)])
    f.close()

def load_csv(name):
    """
    Load csv file and return `X`, `Y`, `xlabel` name and `ylabel` name. 
    
    Parameters
    ----------
        name : str
            name of file
    
    Returns
    -------
        V : dict
            V is a dictionary which contains X and Y values. 
    
    Notes
    -----
    The name of `csv file` `doesn't have` to end with `.csv` or `path`.
    """
    X = list()
    Y = list()
    xlabel = ""
    ylabel = ""
    with open(f'data/{name}.csv', 'r') as f :
        reader = csv.DictReader(f)
        xlabel, ylabel = reader.fieldnames
        for pair in reader:
                X.append(float(pair[xlabel]))
                Y.append(float(pair[ylabel]))
    f.close()
    return {xlabel: X, ylabel: Y} 