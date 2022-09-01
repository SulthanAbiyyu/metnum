import math
# import matplotlib.pyplot as plt

# Masih ada kemungkinan menemui titik stagnant, terjadi bila kurvanya konkaf

def regula_falsi(fx, a, b):
    epsilon = 0.00001
    if fx(a) * fx(b) < 0:

        while abs(a - b) > epsilon:
            c = b - (fx(b) * (b-a))/(fx(b) - fx(a))

            if abs(fx(c)) < epsilon:
                return c
            
            if fx(a) * fx(c) < 0 :
                b = c
            else:
                a = c
        return c

if __name__ == "__main__":
    fx = lambda x: math.e ** x - 5 * x ** 2
    print(regula_falsi(fx, 0, 1))

    # x = [i for i in range(0, 11)]
    # y = [fx(j) for j in x]

    # plt.plot(x, y)
    # plt.show()