"""
Handles csv files (write and read)
"""
import csv
from io import TextIOWrapper

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

def load_csv(csv_file):
    """
    Load csv file and return `X`, `Y`, `xlabel` name and `ylabel` name. 
    
    Parameters
    ----------
        csv_file : str
            csv file
    
    Returns
    -------
        V : dict
            V is a dictionary which contains X and Y values. 
    """
    csv_file = TextIOWrapper(csv_file)
    X = list()
    Y = list()
    xlabel = ""
    ylabel = ""
    print(csv_file)
    reader = csv.DictReader(csv_file)
    print(reader)
    xlabel, ylabel = reader.fieldnames
    for pair in reader:
            X.append(float(pair[xlabel]))
            Y.append(float(pair[ylabel]))
    return {xlabel: X, ylabel: Y} 