from lib2to3.pgen2.token import N_TOKENS
import numpy as np


def power_iteration(A: np.ndarray, x0: np.array, n_iter=100):
    x_new = x0
    for i in range(n_iter):
        dott = np.dot(A, x_new)
        d = dott[np.argmax(np.abs(dott))]
        x_new = dott / d
        print(f"i: {i + 1} | d: {d} | dott: {dott} | x: {x_new}")
    return d, x_new


def power_inverse_iteration(A: np.ndarray, x0: np.array, n_iter=100):
    x_new = x0
    for i in range(n_iter):
        dott = np.dot(A, x_new)
        d = dott[np.argmin(np.abs(dott))]
        x_new = dott / d
        print(f"i: {i + 1} | d: {d} | dott: {dott} | x: {x_new}")
    return d, x_new


if __name__ == "__main__":
    A = np.array([
        [2, 1, 2],
        [1, 3, 2],
        [2, 4, 1]
    ])
    x0 = np.array([1, 1, 1])
    print(power_inverse_iteration(A, x0, n_iter=8))
