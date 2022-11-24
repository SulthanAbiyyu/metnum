def interpolasi_kuadrat(f, a, b, c, n_iter=10):
    fa, fb, fc = f(a), f(b), f(c)
    for _ in range(n_iter):
        d = (f(a) * (b ** 2 - c ** 2) + f(b) * (c ** 2 - a ** 2) + f(c) * (a ** 2 - b ** 2)) / \
            (2 * (f(a) * (b - c) + f(b) * (c - a) + f(c) * (a - b)))

        fd = f(d)

        if d < b:
            if fd > fb:
                c, fc = d, fd
            else:
                a, fa, b, fb = b, fb, d, fd
        elif d > b:
            if fd > fb:
                a, fa = d, fd
            else:
                c, fc, b, fb = b, fb, d, fd
    return d, fd
