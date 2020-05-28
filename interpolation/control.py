"""
Controls interpolation methods and manages X and Y values
"""

import interpolation.methods.linear_system as lys
import interpolation.methods.lagrange as lgr
import interpolation.methods.newton as ntw
import interpolation.methods.cubic_spline as spl

import numpy as np

def create_V(f, start, end, m):
    """
    Create a dictionary for the f function which contains x and y values

    Parameters
    ----------
        f : function
            f(x)
        start : float
            initial value (x)
        end : int
            final value (x)
        m : int
            m values between start param and end param
    
    Returns 
    -------
        dict
            dictionary which contains X and Y values
    """
    X = np.linspace(start, end, m)
    Y = [f(x) for x in X]
    return {'x': X, 'y': Y}

def check_repeat_x(V):
    """
    Check if exists repeated x value

    Parameters
    ----------
        V : dict
            dictionary which contains X and Y values

    Returns
    -------
        bool
            Returns True if there are repeated x's values or 
            False if there are no repeated x's values
    """
    xlabel, _ = V.keys()
    return not(len(V[xlabel]) == len(set(V[xlabel])))

def sort_V(V):
    """
    Sort (x, y) values in ascending order (x)

    Parameters
    ----------
        V : dict
            dictionary which contains X and Y values

    Notes
    -----
    Sorting according to x values
    """
    xlabel, ylabel = V.keys()
    P = list([pair[0], pair[1]] for pair in zip(V[xlabel], V[ylabel]))
    P.sort()
    V[xlabel] = [p[0] for p in P]
    V[ylabel] = [p[1] for p in P]

def interpolation_method(method, X, Y):
    """
    Returns the interpolation function

    Parameters
    ----------
        method : str
            method name
        X : list
            list of x values
        Y : list
            list of y values

    Returns 
    -------
        function
            interpolation function
    
    Notes
    -----
    The interpolation functions are : linear_system, lagrange,
    newton and cubic_spline
    """
    if method == 'linear_system':
        return lsy.linsys(X, Y)
    elif method == 'lagrange':
        return lgr.lagrange(X, Y)
    elif method == 'newton':
        return ntw.newton(X, Y)
    elif method == 'cubic_spline':
        return spl.cubic_spline(X, Y)
    else:
        return None

def interpolation_by_function(f, method, start, stop, n, m):
    """
    Make a interpolation from function f param

    Parameters
    ----------
        f : function
            f(x)
        method : str
            method name
        start : float
            initial value (x)
        end : int
            final value (x)
        n : int
            n values between start param and end param (used by f(x))
        m : int
            m values between start param and end param (used by method function)
    
    Returns
    -------
        dict
            dictionary which contains X and Y values

    Notes
    -----
    The interpolation functions are : linear_system, lagrange,
    newton and cubic_spline
    """
    Xf = np.linspace(start, stop, n).tolist()
    Yf = [f(x) for x in Xf]
    g = interpolation_method(method, Xf, Yf)
    X = np.linspace(start, stop, m)
    Y = [g(x) for x in X]
    return {'x': X, 'y': Y}

def interpolation_by_values(V, method, m):
    """
    Make an interpolation from values (x, y)

    Parameters
    ----------
        V : dict
            dictionary which contains X and Y values
        method : str
            method name
        m : int
            m values between start param and end param (used by method function)

    Returns
    -------
        dict
            dictionary which contains X and Y values
    
    Notes
    -----
    The interpolation functions are : linear_system, lagrange,
    newton and cubic_spline
    """
    if check_repeat_x(V):
        return None
    sort_V(V)
    xlabel, ylabel = V.keys()
    g = interpolation_method(method, V[xlabel], V[ylabel])
    start = V[xlabel][0]
    end = V[xlabel][-1]
    X = np.linspace(start, end, m)
    Y = [g(x) for x in X]
    return {'x': X, 'y': Y}

def string_fx(f, x):
    """
    Return f(x) in string format
    
    Parameters
    ----------
        f : function
            f(x)
        x : float
            value
    
    Returns
    -------
        str
            string format: f(x) = v
    """
    return f'f({x}) = {f(x)}'
