def turunan_kedua(f, x0, h):
    return (f(x0 + h) - 2 * f(x0) + f(x0-h)) / (h ** 2)
