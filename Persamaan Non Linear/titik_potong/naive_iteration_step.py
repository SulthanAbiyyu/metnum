import numpy as np


def naive_iteration_step(f, g, x0, tol=0.1, max_iter=1000, step=1e-3, patience=10):
    xi = x0
    not_updated = 0
    for i in range(max_iter):
        if not_updated > patience:
            return "rage quit!!"

        if abs(abs(f(xi)) - abs(g(xi))) < tol:
            return xi
        else:
            if abs(max(f(xi), g(xi)) - min(f(xi), g(xi))) > abs(max(f(xi + step), g(xi + step)) - min(f(xi + step), g(xi + step))):
                xi += step
            elif abs(max(f(xi), g(xi)) - min(f(xi), g(xi))) > abs(max(f(xi - step), g(xi - step)) - min(f(xi - step), g(xi - step))):
                xi -= step
            else:
                print(f"plateau ke {i+1}")
                not_updated += 1
                # print(f"""
                # plateau at {i + 1} th iteration
                # xi              : {xi}
                # step            : {step}
                # f(x)            : {f(xi)}
                # g(x)            : {g(xi)}
                # Initial point   : {abs(max(f(xi), g(xi)) - min(f(xi), g(xi)))}
                # Step up point   : {abs(max(f(xi + step), g(xi + step)) - min(f(xi + step), g(xi + step)))}
                # Step down point : {abs(max(f(xi - step), g(xi - step)) - min(f(xi - step), g(xi - step)))}
                # """)
    if abs(abs(f(xi)) - abs(g(xi))) > tol:
        return "not solved"


def biyu_initialization(f, g, mode="random", range=(-10, 10), tries=10):

    if mode == "random":
        x = np.random.randint(range[0], range[1], size=(tries))
    elif mode == "linspace":
        x = np.linspace(range[0], range[1])
    elif mode == "arange":
        x = np.arange(range[0], range[1])

    closest_point = [0, 9999]  # index, min_val
    for idx, xi in enumerate(x):

        y_max = max(f(xi), g(xi))
        y_min = min(f(xi), g(xi))
        length = abs(y_max - y_min)

        if length < closest_point[1]:
            closest_point[0] = idx
            closest_point[1] = length

    return x[closest_point[0]]


if __name__ == "__main__":
    # def f(x): return x ** 2 - 1
    # def g(x): return x ** 3

    # def f(x): return x ** 2
    # def g(x): return x ** 3

    def f(x): return ((x ** 2) / 2) + x - 2
    def g(x): return x ** 3

    x0 = biyu_initialization(f, g, mode="linspace")
    x_tipot = naive_iteration_step(f, g, x0, step=1e-3)
    print(x0)
    print(x_tipot)
    # print(
    #     f"x0 = {x0} \t x_tipot = {x_tipot} \nf(x) = {f(x_tipot)} \t g(x) = {g(x_tipot)}")

    # # experiment
    # divirgent = 0
    # not_solved = 0

    # TRIES = 10
    # PATIENCE = 10
    # MAX_ITER = 1_000
    # STEP = 1e-3
    # ITERATION = 100

    # # random seed
    # for i in range(ITERATION):
    #     x0 = biyu_initialization(f, g, tries=TRIES)
    #     x_tipot = naive_iteration_step(
    #         f, g, x0, max_iter=MAX_ITER, step=STEP, patience=PATIENCE)
    #     print(
    #         f"\n\nx0 = {x0} \t x_tipot = {x_tipot: .3f} \nf(x) = {f(x_tipot): .3f} \t g(x) = {g(x_tipot): .3f}")

    #     if x_tipot == -1:
    #         divirgent += 1
    #     elif x_tipot == -2:
    #         not_solved += 1

    # print(f"divirgent rate: {divirgent / ITERATION}")
    # print(f"Not solved rate: {not_solved / ITERATION}")
