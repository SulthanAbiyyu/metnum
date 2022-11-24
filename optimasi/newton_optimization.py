import numpy as np


def newton_optimization(fx, x0, n_iter: int = 10):

    def diff(f, x, h=0.0001):
        return (8 * f(x + h) - 8 * f(x - h) - (f(x + 2*h) - f(x - 2*h))) / (12 * h)

    def second_diff(f, x, h=0.0001):
        return 1/h**2 * (f(x-h) - 2*f(x) + f(x+h))
    for _ in range(n_iter):
        x0 = x0 - (diff(fx, x0) / second_diff(fx, x0))

    return x0


if __name__ == "__main__":
    x = 2.5

    def g(x): return 2 * np.sin(x) - (x ** 2 / 10)

    print(newton_optimization(g, x, n_iter=4))
