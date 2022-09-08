import numpy as np

from penyulihan_mundur import penyulihan_mundur


def naive_gauss_jordan(A: np.ndarray, b: np.array) -> np.array:
    n = b.shape[0]
    for k in range(0, n):  # looping tiap baris pivot
        # Membagi baris pivot dengan nilai pivot biar mudah (jadi 1)
        initial_pivot = A[k][k]
        for j in range(0, n):
            A[k][j] = A[k][j] / initial_pivot

        b[k] = b[k] / initial_pivot

        # eliminasi tiap barisnya, tapi i != k soalnya masak ngurangin pivotnya :D
        for i in range(0, n):
            if i != k:
                # karena tadi pivotnya udah dibagi, jadinya langsung aja
                m = A[i][k]
                for j in range(0, n):
                    A[i][j] = A[i][j] - m * A[k][j]
                b[i] = b[i] - m * b[k]

    return b


if __name__ == "__main__":
    A = np.array([
        [3, -0.1, -0.2],
        [0.1, 7, -0.3],
        [0.3, -0.2, 10]
    ])
    b = np.array([7.85, -19.3, 71.4])

    print(naive_gauss_jordan(A, b))
