import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns


def naive_iteration_step(f, g, x0, tol=0.1, max_iter=1000, step=1e-3, patience=10):
    xi = x0
    x0s = []
    x0s.append(xi)
    not_updated = 0
    for i in range(max_iter):
        if not_updated > patience:
            return "rage quit!!", x0s

        if abs(f(xi) - g(xi)) < tol:
            return xi, x0s
        else:
            # print(
            # f"Initial point   : {abs(max(f(xi), g(xi)) - min(f(xi), g(xi)))}")
            # print(
            # f"Step up point   : {abs(max(f(xi + step), g(xi + step)) - min(f(xi + step), g(xi + step)))}")
            # print(f"xi: {xi} \n xi+step: {xi+step}")
            if abs(max(f(xi), g(xi)) - min(f(xi), g(xi))) > abs(max(f(xi + step), g(xi + step)) - min(f(xi + step), g(xi + step))):
                xi += step
                # print("maju")
                x0s.append(xi)
            elif abs(max(f(xi), g(xi)) - min(f(xi), g(xi))) > abs(max(f(xi - step), g(xi - step)) - min(f(xi - step), g(xi - step))):
                xi -= step
                # print("mundur")
                x0s.append(xi)
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
    if abs(f(xi) - g(xi)) > tol:
        return "not solved", x0s


def biyu_initialization(f, g, mode="random", range=(-10, 10), tries=10):

    if mode == "random":
        x = np.random.randint(range[0], range[1], size=(tries))
    elif mode == "linspace":
        x = np.linspace(range[0], range[1])
    elif mode == "arange":
        x = np.arange(range[0], range[1])

    closest_point = [0, 0]  # index, min_val
    for idx, xi in enumerate(x):

        y_max = max(f(xi), g(xi))
        y_min = min(f(xi), g(xi))
        length = abs(y_max - y_min)

        if idx == 0:
            closest_point[1] = length

        if length < closest_point[1]:
            closest_point[0] = idx
            closest_point[1] = length

    return x[closest_point[0]]


if __name__ == "__main__":
    # def f(x): return x ** 2 - 1
    # def g(x): return x ** 3

    # def f(x): return x ** 2
    # def g(x): return x ** 3

    # # Polinomial tests

    def f(x): return x ** 4 + 2 * x ** 3 - 2 * x ** 2 - x - 2
    def g(x): return x

    x0 = biyu_initialization(f, g, mode="linspace")
    x_tipot, _ = naive_iteration_step(f, g, 1, max_iter=1000, tol=0.01)
    print(x0)
    print(x_tipot)
    print(f(x_tipot))

    # linspace mode [-10, 10] failed because of little bump in the middle

    # # Visualisasi

    # def f(x): return ((x ** 2) / 2) + x - 2
    # def g(x): return x ** 3

    # x = np.linspace(-10, 10)
    # fx = f(x)
    # gx = g(x)

    # x0 = biyu_initialization(f, g, mode="linspace")
    # x_tipot, x0s = naive_iteration_step(f, g, x0, step=1e-3, tol=1e-2)
    # print(x0)
    # print(x_tipot)

    # x0s = np.array(x0s)
    # fx0s = f(x0s)
    # gx0s = g(x0s)

    # sns.lineplot(x=x, y=fx, label="f(x)")
    # sns.scatterplot(x=x0s, y=fx0s, label="f(x0s)")
    # sns.scatterplot(x=x0s, y=gx0s, label="g(x0s)")
    # sns.lineplot(x=x, y=gx, label="g(x)")
    # plt.grid(True)
    # plt.xlim([-2, 0])
    # plt.ylim([-3, -2])
    # plt.legend()
    # plt.show()

    # # Experiment

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
