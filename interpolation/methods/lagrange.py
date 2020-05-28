"""
Lagrange (Polynomial Interpolation)
"""

import numpy as np

def L(i, X):
    """
    This function returns l(x).

    Parameters
    ----------
        i : int
            Index of X.
        X : list
            List of x values.

    Returns
    -------
        function
            l(x) 
    """ 
    temp = X.copy()
    xi = temp.pop(i)

    def l(x):
        return np.prod([(x - xj) / (xi - xj) for xj in temp])

    return l

def lagrange(X, Y):
    """
    Polynomial Interpolation using Lagrange method.
    X and Y are data from `(x, f(x))`.

    Parameters
    ----------
        X : list
            list of x values.
        Y : list
            list of y values.

    Returns 
    -------
        function
            Lagrange Polynomial from `X` and `Y` values.            
    """
    def f(x):
        return sum([yi * L(i, X)(x) for i, yi in enumerate(Y)])

    return f