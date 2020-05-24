import methods.linsys as linsys
import methods.lagrange as lgr
import methods.newton as ntw
from matplotlib import pyplot as plt
import numpy as np 

def check_repeat_x(x):
    """
    Check if exists repeated x value
    @return True -> there are repeated x's values
            False -> there are no repeated x's values
    """
    return not(len(x) == len(set(x)))

def string_fx(f, x):
    """
    Return the function value in string -> f(x) = a
    """
    return f'f({x}) = {f(x)}'

x1 = [-1, 0, 2]
y1 = [4, 1, -1]
