def heun_correction(f, x0, y0, h, target):
    n = int((target - x0) / h)
    y = y0
    x = x0
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h, y + h*k1)
        y = y + h*(k1 + k2)/2
        x = x + h
    return y


def heun_correction_expansion(f, x0, y0, h, target, epsilon=1e-6):
    n = int((target - x0) / h)
    y = y0
    x = x0
    for _ in range(n):
        y_temp = y
        y = y + h*f(x, y)
        tampung = y
        while abs(y - tampung) > epsilon:
            tampung = y
            y = y_temp + h/2 * (f(x, y_temp) + f(x + h, y))
        x += h
    return y


if __name__ == "__main__":
    def f(x, y): return x + y
    x0 = 0
    y0 = 1
    h = 0.05
    target = 0.1
    y = heun_correction(f, x0, y0, h, target)
    y2 = heun_correction_expansion(f, x0, y0, h, target)
    print(y)
    print(y2)
