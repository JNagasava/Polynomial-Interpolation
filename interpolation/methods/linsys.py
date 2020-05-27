import numpy as np 

def swap_rows(Z, a, b):
    """
    Swap two rows (a, b) of a matrix 
    """
    temp = np.copy(Z[a])
    Z[a] = Z[b]
    Z[b] = temp

def partial_pivoting(Z, row):
    """
    Partial pivoting of Z matrix, starting at row(parameter)
    @return pivot
    """
    pivot_row = np.argmax(np.abs(Z[row:, row])) + row
    swap_rows(Z, row, pivot_row)
    pivot = Z[row, row]
    return pivot

def solve_sys(X, Y):
    """
    Solve a linear system using Gauss Elimination
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

def vandermond(x):
    """
    Create a vandermond matrix(nxn) by x's values  
    """
    n = len(x)
    V = np.zeros((n, n))

    for i in range(n):
        V[i, :] = [x[i]**k for k in range(n)]

    return V

def polynomial(A):
    """
    Create the polynomial function
    """
    def f(x):
       return sum([a*(x**p) for p, a in enumerate(A)])

    return f

def linsys(X, Y):
    """
    Polynomial Interpolation using Gauss Elimination
    """
    V = vandermond(X)
    A = solve_sys(V, Y)
    return polynomial(A)
    

        


    