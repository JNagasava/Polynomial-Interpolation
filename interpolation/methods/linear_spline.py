import numpy as np
from bisect import bisect_right

def Sk(X, Y, k):
    """
    Create Sk function

    Parameters
    ----------
        X : list
            list of x values
        Y : list
            list of y values
        k : int
            index from X and Y
    
    Returns
    -------
        function
            Sk from linear spline
    """

    def f(x):
        if(X[k + 1] != X[k]):
            return Y[k] * ((X[k + 1] - x)/(X[k + 1] - X[k])) + Y[k + 1] * ((x - X[k])/(X[k + 1] - X[k]))
    
    return f

def linear_spline(X, Y):
    """
    Polynomal Interpolation by parts using a linear spline

    Parameters
    ----------
        X : list
            list of x values
        Y : list
            list of y values
    
    Returns
    -------
        function
            function of interpolation by parts (using linear spline)
    """

    n = len(X)

    S = [Sk(X, Y, k) for k in range(n)]

    def f(x):
        k =  bisect_right(X, x) - 1
        if k == (n - 1):
            k -= 1
        return S[k](x)
    
    return f



