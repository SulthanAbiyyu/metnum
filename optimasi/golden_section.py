from numpy import sqrt, sin


def golden_section(f, a, b, n_iter=17):

    for _ in range(n_iter):
        d = (sqrt(5) - 1) / 2 * (b-a)
        x1 = a + d
        x2 = b - d

        if f(x1) > f(x2):
            a = x2
        elif f(x1) < f(x2):
            b = x1

    return (a + b) / 2


if __name__ == "__main__":
    def g(x): return 2 * sin(x) - (x ** 2 / 10)

    print(golden_section(g, 0, 4))
