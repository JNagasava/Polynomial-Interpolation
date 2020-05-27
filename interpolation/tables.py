import csv

def create_csv(X, Y, xlabel, ylabel, name):
    """
    Create csv file by X and Y values 
    """
    with open(f'data/{name}.csv', 'w') as f :
        writer = csv.DictWriter(f, fieldnames=[f'{xlabel}', f'{ylabel}'])
        writer.writeheader()
        writer.writerows([{f'{xlabel}': pair[0], f'{ylabel}': pair[1]} for pair in zip(X, Y)])
    f.close()

def load_csv(name):
    """
    Load csv file and return X, Y, xlabel name and ylabel name 
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