import methods.linsys as linsys
import methods.lagrange as lgr
import methods.newton as ntw
import methods.spline as spline
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

x2 = [-2, -1, 0, 1, 2]
y2 = [-15, 0, 3, 0, -3]

x3 = [0, 1/4, 1/2, 3/4, 1]
y3 = [1, 2, 1, 0, 1]

x4 = [0, 0.5, 1, 1.5, 2]
y4 = [3, 1.8616, -0.5571, -4.1987, -9.0536]

f = spline.cubic_spline(x4, y4)

print(string_fx(f, 0.35))

# f = ntw.newton(x2, y2)

# print(string_fx(f, -2))
# print(string_fx(f, -1))
# print(string_fx(f, 0))
# print(string_fx(f, 1))
# print(string_fx(f, 2))

# x = np.linspace(-2, 2, 100)

# plt.plot(x, [f(k) for k in x])

# plt.grid()

# plt.show()

