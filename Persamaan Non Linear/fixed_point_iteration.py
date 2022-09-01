import math

def fp(gx, x):
    n_maks = 30
    epsilon = 0.00001
    x_lama = 999
    n = 0

    while abs(x-x_lama) > epsilon or n < n_maks:
        x_lama = x
        x = gx(x)
        n += 1
    
    if n > n_maks:
        print("divergen?")
    return x, n

if __name__ == "__main__":
    fx = lambda x: x ** 2 - 2 * x - 3
    gx = lambda x: math.sqrt(2 * x + 3) # g(x) adalah bentuk x = g(x) dari f(x) = 0

    print(fp(gx, x=4))

