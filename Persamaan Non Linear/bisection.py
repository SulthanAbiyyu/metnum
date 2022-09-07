import matplotlib.pyplot as plt

def bisection(fx, a, b):

    epsilon1 = 0.000001
    if fx(a) * fx(b) < 0:
        while abs(a-b) > epsilon1:
            c = (a + b) / 2
            if fx(a) * fx(c) < 0:
                b = c
            elif fx(a) * fx(c) > 0:
                a = c
        return c
    else:
        raise ValueError


if __name__ == "__main__":
    def fx(x): return x**3 - 2 * (x**2) + 6*x - 4.0
    print(bisection(fx, -3, 2))

    x = [i for i in range(-3, 3)]
    y = [fx(i) for i in x]

    plt.plot(x, y)
    plt.show()
