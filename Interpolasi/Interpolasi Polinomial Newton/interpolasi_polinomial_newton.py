import numpy as np


def membuat_ST(x, y):
    n = len(x)
    ST = np.zeros((n, n))
    for k in range(n):
        ST[k][0] = y[k]
    for k in range(1, n):
        for i in range(0, n-k):
            ST[i][k] = (ST[i+1][k-1] - ST[i][k-1]) / (x[i+k] - x[i])

    return ST


def newton_polynom(x_input, ST):
    jumlah = ST[0][0]
    n = len(ST[0])
    for i in range(1, n):
        suku = 0
        a_i = ST[0][i]
        suku = suku + a_i
        for k in range(0, i-1):
            suku = suku * (x_input-x[k])

        jumlah = jumlah + suku

    y_newton = jumlah
    return y_newton


x = [8.0, 9.0, 9.5, 11.0]
y = [2.079442, 2.197225, 2.251292, 2.397895]

ST = membuat_ST(x, y)
print(newton_polynom(9.2, ST))
