import numpy as np 
import methods.linsys as linsys
from bisect import bisect_right

def Ak(Y2d, H, k):
    """
    Calculate Ak for Sk(x)    
    """
    return (Y2d[k] - Y2d[k - 1]) / (6 * H[k - 1])

def Bk(Y2d, k):
    """
    Calculate Bk for Sk(x)
    """
    return Y2d[k] / 2

def Ck(Y2d, H, Y, k):
    """
    Calculate Ck for Sk(x)
    """
    return (Y[k] - Y[k - 1]) / H[k - 1] + (2 * H[k - 1] * Y2d[k] + Y2d[k - 1] * H[k - 1]) / 6 

def Dk(Y, k):
    """
    Calculate Dk for Sk(x)
    """
    return Y[k]

def Hk(X, k):
    """
    Calculate Hk for Sk(x)
    """
    return X[k] - X[k - 1]

def Sk(Y2d, H, X, Y, k):
    """
    Create Sk function
    """
    def f(x):
        x_diff = x - X[k]
        a = Ak(Y2d, H, k) * x_diff**3
        b = Bk(Y2d, k) * x_diff**2
        c = Ck(Y2d, H, Y, k) * x_diff
        d = Dk(Y, k)
        return a + b + c + d
    return f

def cubic_spline(X, Y):
    """
    Polynomal Interpolation by parts using a natural cubic spline
    """

    # H's
    n = len(X)
    H = [Hk(X, k) for k in range(1, n)]
    
    # A
    m = n - 2
    A = np.zeros((m, m))
    
    # Diagonal (A)
    np.fill_diagonal(A, [2 * (H[k] + H[k + 1]) for k in range(m)])  
    # Upper and lower diagonal (A)
    for k in range(0, m - 1):
        A[k, k + 1] = H[k + 1]                                          
        A[k + 1, k] = H[k + 1]                                          

    # B
    B = [ 6 * ((Y[k + 2] - Y[k + 1]) / H[k + 1] - (Y[k + 1] - Y[k]) / H[k]) for k in range(m)]

    # Y2d
    Y2d = linsys.solve_sys(A, B)

    Y2d = [0, *Y2d, 0]

    S = [Sk(Y2d, H, X, Y, k) for k in range(1, n)]

    def f(x):
        k = bisect_right(X, x) - 1
        if k == n - 1:
            k -= 1
        return S[k - 1](x)

    return f

