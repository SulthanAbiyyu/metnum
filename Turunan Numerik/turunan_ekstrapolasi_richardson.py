import numpy as np


def turunan_ekstrapolasi_richardson(f, x0, h):
    return (8 * f(x0 + h) - 8 * f(x0 - h) - (f(x0 + 2*h) - f(x0 - 2*h))) / (12 * h)


if __name__ == "__main__":
    print(turunan_ekstrapolasi_richardson(lambda x: np.tan(x), 1, 0.5))
