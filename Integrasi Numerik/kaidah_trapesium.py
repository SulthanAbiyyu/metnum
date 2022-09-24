def kaidah_trapesium(f, a, b, n):
    """
    Args
    f: fungsi
    a: lower bound
    b: upper bound
    n: banyaknya strip
    """

    lebar = (b-a)/ n
    xi = a
    integral = f(a) + f(b)
    sigma = 0

    for _ in range(1, b):
        xi += lebar
        sigma += 2 * f(xi)

    integral = (integral + sigma) * lebar / 2
    
    
    print((sigma + integral) * lebar)

    return integral

if __name__ == "__main__":
    f = lambda x: x ** 2 + 1
    print(kaidah_trapesium(f, 0, 2, 10))

