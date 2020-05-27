import numpy as np 

def newton(X, Y):
    """
    Polynomial Interpolation using Newton's method
    """
    n = len(X)
    K = np.zeros((n, n))
    K[:, 0] = Y

    for k in range(1, n):
        K[k:, k] = [(K[i, k - 1] - K[i - 1, k - 1]) / (X[i] - X[i - k]) for i in range(k, K.shape[0])]
    D = np.ndarray.tolist(np.diag(K))

    def f(x):
        A = np.ones((n))
        A[1: n] = [(x - X[k]) for k in range(n - 1)]
        return sum(D[i] * np.prod(A[: i + 1]) for i in range(n))

    return f
