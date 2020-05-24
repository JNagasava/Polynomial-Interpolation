import numpy as np

def L(i, X):
    """
    Calculate L's of Lagrange method
    @return L (function)
    """ 
    temp = X.copy()
    xi = temp.pop(i)

    def l(x):
        return np.prod([(x - xj) / (xi - xj) for xj in temp])

    return l
        

def lagrange(X, Y):
    """
    Polynomial Interpolation using Lagrange method
    @return Lagrange Polynom (function)
    """
    def f(x):
        return sum([yi * L(i, X)(x) for i, yi in enumerate(Y)])

    return f


