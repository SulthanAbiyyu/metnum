def naive_iteration_step(f, g, x0, tol=0.1, max_iter=1000, step=0.1):
    xi = x0
    for _ in range(max_iter):
        if abs(f(xi) - g(xi)) < tol:
            break
        else:
            if abs((f(xi) - g(xi))) > abs(f(xi + step) - g(xi + step)):
                xi += step
            elif abs(f(xi) - g(xi)) > abs(f(xi - step) - g(xi - step)):
                xi -= step
            else:
                print("plateau")
    return xi

if __name__ == "__main__":
    f = lambda x: x ** 2 - 1
    g = lambda x: x ** 3

    x_tipot = naive_iteration_step(f, g, 0)
    print(x_tipot)
    print(f(x_tipot))
    print(g(x_tipot))
