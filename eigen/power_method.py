from lib2to3.pgen2.token import N_TOKENS
import numpy as np


def power_iteration(A: np.ndarray, x0: np.array, n_iter=100):
    x_new = x0
    for _ in range(n_iter):
        dott = np.dot(A, x_new)
        d = dott[np.argmax(np.abs(dott))]
        x_new = dott / d
    return x_new


if __name__ == "__main__":
    A = np.array([
        [5, -2],
        [7, -4]
    ])
    x0 = np.array([1, 3])
    print(power_iteration(A, x0, n_iter=28))
