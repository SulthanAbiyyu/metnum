def naive_iteration_step(f, g, x0, tol=0.1, max_iter=1000, step=0.1):
    xi = x0
    for i in range(max_iter):
        if abs(f(xi) - g(xi)) < tol:
            break
        else:
            if abs(max(f(xi), g(xi)) - min(f(xi), g(xi))) > abs(max(f(xi + step), g(xi + step)) - min(f(xi + step), g(xi + step))):
                xi += step
            elif abs(max(f(xi), g(xi)) - min(f(xi), g(xi))) > abs(max(f(xi - step), g(xi - step)) - min(f(xi - step), g(xi - step))):
                xi -= step
            else:
                print(f"plateau at {i + 1} th iteration")
    return xi

def initialization

if __name__ == "__main__":
    def f(x): return x ** 2 - 1
    def g(x): return x ** 3

    x_tipot = naive_iteration_step(f, g, -0.5, max_iter=1_000_000, step=1e-5)
    print(x_tipot)
    print(f(x_tipot))
    print(g(x_tipot))
