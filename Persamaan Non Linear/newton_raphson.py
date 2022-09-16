import numpy as np


def f(x): return x ** 3 - 2 * x ** 2 + x + 0.5


def grad(f, x, h=1e-4):
    return (f(x+h)-f(x-h))/(2*h)


def loss_fn(x_old, x_new):
    return abs(abs(x_old) - abs(x_new))


def backward(f, x):
    x_new = x - (((f(x)) / grad(f, x)))
    return x_new


if __name__ == "__main__":
    x0 = 2.10
    loss = 1
    epsilon = 1e-4
    n_upper = 11
    for i in range(1, n_upper):
        hasil = backward(f, x0)
        loss = loss_fn(x0, hasil)
        print(f"Iterasi {i} | x_new = {hasil} | x_old = {x0} | loss = {loss}")

        if loss < epsilon:
            break

        x0 = hasil
