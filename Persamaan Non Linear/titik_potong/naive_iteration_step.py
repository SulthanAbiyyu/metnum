import numpy as np


def naive_iteration_step(f, g, x0, tol=0.1, max_iter=1000, step=0.1, patience=10):
    xi = x0
    not_updated = 0
    for _ in range(max_iter):
        if not_updated > patience:
            # print("Wrong initialization")
            return -1

        if abs(f(xi) - g(xi)) < tol:
            return xi
        else:
            if abs(max(f(xi), g(xi)) - min(f(xi), g(xi))) > abs(max(f(xi + step), g(xi + step)) - min(f(xi + step), g(xi + step))):
                xi += step
            elif abs(max(f(xi), g(xi)) - min(f(xi), g(xi))) > abs(max(f(xi - step), g(xi - step)) - min(f(xi - step), g(xi - step))):
                xi -= step
            else:
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
        return -2


def biyu_initialization(f, g, tries=3, range=(-10, 10)):
    x = np.random.randint(range[0], range[1], size=(tries))
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
    def f(x): return x ** 2 - 1
    def g(x): return x ** 3

    # experiment
    divirgent = 0
    not_solved = 0
    for i in range(100):
        x0 = biyu_initialization(f, g, tries=10)
        x_tipot = naive_iteration_step(f, g, x0, max_iter=1_000, step=3e-4)
        # print(
        #     f"x0 = {x0} \t x_tipot = {x_tipot: .3f} \nf(x) = {f(x_tipot): .3f} \t g(x) = {g(x_tipot): .3f}")

        if x_tipot == -1:
            divirgent += 1
        elif x_tipot == -2:
            not_solved += 1

    print(f"divirgent rate: {divirgent / 100}")
    print(f"Not solved rate: {not_solved / 100}")
