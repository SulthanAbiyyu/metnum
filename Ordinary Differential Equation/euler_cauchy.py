import numpy as np


def euler_cauchy(f, x0, y0, h, target):
    n = int((target - x0) / h)
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    x[0] = x0
    y[0] = y0
    for i in range(n):
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h*f(x[i], y[i])
    return x, y


def get_y_euler(x: np.array, y: np.array) -> tuple:
    return x[-1], y[-1]


if __name__ == "__main__":
    def f(x, y): return x + y
    x0 = 0
    y0 = 1
    h = 0.05
    target = 0.1
    x, y = euler_cauchy(f, x0, y0, h, target)
    print(x)
    print(y)
    print(get_y_euler(x, y))
