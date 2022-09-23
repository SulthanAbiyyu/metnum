import numpy as np


def naive_iteration_step(f, g, x0, tol=0.1, max_iter=1000, step=0.1):
    xi = x0
    for i in range(max_iter):
        if abs(f(xi) - g(xi)) < tol:
            break
        else:
            if abs(max(f(xi), g(xi)) - min(f(xi), g(xi))) > abs(max(f(xi + step), g(xi + step)) - min(f(xi + step), g(xi + step))):
                xi += step
            elif abs(max(f(xi), g(xi)) - min(f(xi), g(xi))) > abs(max(f(xi - step), g(xi - step)) - min(f(xi - step), g(xi - step))):
                xi -= step
            else:
                print(f"plateau at {i + 1} th iteration")
    return xi


def biyu_initialization(f, g, tries=3, range=(-10, 10)):
    x = np.random.randint(range[0], range[1], size=(tries))

    closest_point = [0, 9999]  # index, min_val
    for idx, xi in enumerate(x):
        y_max = max(f(xi), g(xi))
        y_min = min(f(xi), g(xi))
        length = abs(y_max - y_min)

        if length < closest_point[1]:
            closest_point[0] = idx
            closest_point[1] = xi

    return x[closest_point[0]]


if __name__ == "__main__":
    def f(x): return x ** 2 - 1
    def g(x): return x ** 3

    x0 = biyu_initialization(f, g, tries=10)
    x_tipot = naive_iteration_step(f, g, -0.5, max_iter=1_000_000, step=1e-5)
    print(x_tipot)
    print(f(x_tipot))
    print(g(x_tipot))
