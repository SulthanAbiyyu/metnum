def polinom_lagrange(x_input, x, y):
    n = len(x) - 1
    L = 0
    for i in range(n):
        pi = 1
        for j in range(n):
            if i != j:
                pi = pi * (x_input - x[j]) / (x[i] - x[j])
        L = L + y[i]*pi

    return L


x = [1, 4, 6]
y = [1.5709, 1.5727, 1.5751]

print(polinom_lagrange(3.5, x, y))
