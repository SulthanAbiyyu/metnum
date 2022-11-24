import numpy as np
from newton_optimization import newton_optimization
from typing import Callable


def steepest_descent_ascent(fxy: Callable, X: np.array, n_iter: int = 100, verbose=False) -> np.array:
    def diff(f, x, h=0.0001):
        return (8 * f(x + h) - 8 * f(x - h) - (f(x + 2*h) - f(x - 2*h))) / (12 * h)

    def gradient(f, X, h=0.0001):
        return np.array([diff(lambda x: f(x, X[1]), X[0], h), diff(lambda y: f(X[0], y), X[1], h)])

    for _ in range(n_iter):
        def g(h):
            return fxy(X[0] + gradient(fxy, X)[0] * h, X[1] + gradient(fxy, X)[1] * h)

        h = newton_optimization(g, 0.5)
        X = X + gradient(fxy, X) * h
        if verbose:
            print(X)
    return X


if __name__ == "__main__":
    # fxy = lambda x, y: x ** 2 + y ** 2 + 2 * x + 4
    def fxy(x, y): return 2 * x * y + 2*x - x ** 2 - 2 * y ** 2

    # X = np.array([2, 1])
    X = np.array([-1, 1])

    steepest_descent_ascent(fxy, X, n_iter=13, verbose=True)
