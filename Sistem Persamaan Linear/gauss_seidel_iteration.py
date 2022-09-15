from random import gauss
import numpy as np


def gauss_seidel_iteration(A: np.ndarray, b: np.array, x: np.array):
    n = b.shape[0]
    epsilon = 0.0001

    konvergen = False
    x_lama = np.copy(x)

    while (not konvergen):
        # looping tiap x_i
        for i in range(0, n):
            x_lama[i] = np.copy(x[i])
            sigma_1 = 0
            for j in range(0, i):
                # Ini hitung yang pake x baru
                sigma_1 = sigma_1 - A[i][j] * x[j]

            sigma_2 = 0
            for j in range(i, n):
                sigma_2 = sigma_2 + A[i][j] * x[j]  # ini sisanya

            x[i] = (b[i] - sigma_1 - sigma_2) / \
                A[i, i]  # nahh ini langsung diupdate

        # cek konvergensi
        for k in range(0, n):
            if abs(x_lama[k] - x[k]) > epsilon:
                print("dor")
                break
        else:
            konvergen = True

    return x


if __name__ == "__main__":
    A = np.array([
        [4, -1, 1],
        [4, -8, 1],
        [-2, 1, 5]
    ])

    b = np.array([7., -21., 15])
    x0 = np.array([1., 2., 2.])

    print(gauss_seidel_iteration(A, b, x0))
