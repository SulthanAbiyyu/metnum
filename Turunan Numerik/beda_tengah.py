import numpy as np


def beda_tengah(f, x0, h):
    return (f(x0+h)-f(x0-h))/(2*h)


if __name__ == "__main__":
    print(beda_tengah(lambda x: np.sin(x)/x, 1, 0.5))
