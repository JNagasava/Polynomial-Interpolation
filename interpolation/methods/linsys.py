"""
Linear System (Polynomial Interpolation)
"""

import numpy as np 

def swap_rows(Z, a, b):
    """
    Swap two rows (a, b) from Z matrix (np.array)

    Parameters
    ----------
        Z : np.array
            matrix
        a : int
            index row from Z
        b : int 
            index row from Z 
    """
    temp = np.copy(Z[a])
    Z[a] = Z[b]
    Z[b] = temp

def partial_pivoting(Z, row):
    """
    Partial pivoting of Z matrix, starting at row param

    Parameters
    ----------
        Z : np.array
            matrix
        row : int
            index row from Z
    
    Returns
    -------
        pivot : int
            pivot is the max value from Z(row:,row)
    """
    pivot_row = np.argmax(np.abs(Z[row:, row])) + row
    swap_rows(Z, row, pivot_row)
    pivot = Z[row, row]
    return pivot

def solve_sys(X, Y):
    """
    Solve a linear system using Gauss Elimination

    Parameters
    ----------
        X : list
            list of x values
        Y : list
            list of y values

    Returns
    -------
        list
            returns the roots of linear system (X, Y)
    """
    Z = np.copy(X)
    Z = np.hstack([Z, np.transpose(np.array([Y]))])

    for j in range(Z.shape[0] - 1):
        pivot = partial_pivoting(Z, j)
        for i in range(j + 1, Z.shape[0]):
            if Z[i, j] != 0 : 
                m = pivot / Z[i, j]
                Z[i, j:] = Z[j, j:] - (m * Z[i, j:])

    A = np.zeros((X.shape[0], 1))
    for k in range(Z.shape[0] - 1, -1, -1):
        A[k] = (Z[k, Z.shape[1]-1] - (Z[k, Z.shape[1]-2:k:-1] @ A[A.shape[0]:k:-1])) / Z[k, k]
    
    return np.ndarray.tolist(np.transpose(A))[0]

def vandermond(X):
    """
    Create a vandermond matrix(nxn) by x values  

    Parameters
    ----------
        X : list
            list of x values

    Returns
    -------
        np.array
            vandermond matrix
    """
    n = len(X)
    V = np.zeros((n, n))

    for i in range(n):
        V[i, :] = [X[i]**k for k in range(n)]

    return V

def linsys(X, Y):
    """
    Polynomial Interpolation using Gauss Elimination

    Parameters
    ----------
        X : list
            list of X values
        Y : list
            list of Y values
    
    Returns
    -------
        function
            function of polynomial interpolation (using linear system)
    """
    V = vandermond(X)
    A = solve_sys(V, Y)

    def f(x):
       return sum([a*(x**p) for p, a in enumerate(A)])

    return f
    

        


    