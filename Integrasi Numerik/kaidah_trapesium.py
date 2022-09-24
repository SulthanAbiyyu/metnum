def kaidah_trapesium(f, a, b, n):
    """
    Args
    f: fungsi
    a: lower bound
    b: upper bound
    n: banyaknya strip
    """

    lebar = (b-a) / n
    integral = 0.5 * (f(a) + f(b))
    sigma = 0

    for i in range(1, n):
        sigma += f(a + i * lebar)

    integral = (integral + sigma) * lebar

    return integral


if __name__ == "__main__":
    def f(x): return x ** 2 + 1
    print(kaidah_trapesium(f, 0, 2, 10))
