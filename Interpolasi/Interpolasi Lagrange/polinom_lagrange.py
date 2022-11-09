def polinom_lagrange(x_input, x, y):
    n = len(x) - 1
    # n = 3
    L = 0
    for i in range(n):
        pi = 1
        for j in range(n):
            if i != j:
                pi = pi * (x_input - x[j]) / (x[i] - x[j])

        L = L + y[i]*pi

    return L


x = [40, 50, 60, 70, 80, 90]
y = [180, 204, 226, 250, 276, 304]

print(polinom_lagrange(84, x, y))
