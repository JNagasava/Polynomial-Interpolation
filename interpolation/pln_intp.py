import methods.linsys as lsy
import methods.lagrange as lgr
import methods.newton as ntw
import methods.spline as spl

import numpy as np

def check_repeat_x(V):
    """
    Check if exists repeated x value
    @return True -> there are repeated x's values
            False -> there are no repeated x's values
    """
    xlabel, _ = V.keys()
    return not(len(V[xlabel]) == len(set(V[xlabel])))

def sort_V(V):
    """
    Sort (x, y) values in ascending order (x)
    """
    xlabel, ylabel = V.keys()
    P = list([pair[0], pair[1]] for pair in zip(V[xlabel], V[ylabel]))
    P.sort()
    V[xlabel] = [p[0] for p in P]
    V[ylabel] = [p[1] for p in P]

def function_method(method, X, Y):
    """
    Returns the method function
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
    Make a interpolation by a function
    """
    Xf = np.linspace(start, stop, n).tolist()
    Yf = [f(x) for x in Xf]
    g = function_method(method, Xf, Yf)
    X = np.linspace(start, stop, m)
    Y = [g(x) for x in X]
    return {'x': X, 'y': Y}

def interpolation_by_values(V, method, m):
    """
    Make an interpolation by values (x, y)
    """
    if check_repeat_x(V):
        return None
    sort_V(V)
    xlabel, ylabel = V.keys()
    g = function_method(method, V[xlabel], V[ylabel])
    start = V[xlabel][0]
    end = V[xlabel][-1]
    X = np.linspace(start, end, m)
    Y = [g(x) for x in X]
    return {'x': X, 'y': Y}

def string_fx(f, x):
    """
    Return the function value in string -> f(x) = a
    """
    return f'f({x}) = {f(x)}'
