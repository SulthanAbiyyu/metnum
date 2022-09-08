import numpy as np

from penyulihan_mundur import penyulihan_mundur


def naive_gauss_elimination(A, b, n) -> np.ndarray:
    for k in range(0, n-1):  # baris pivot
        for i in range(k+1, n):  # eliminasi berdasarkan pivotnya
            m = A[i][k] / A[k][k]  # elemen pembagi
            for j in range(k, n):  # eliminasi tiap elemen
                A[i][j] = A[i][j] - m * A[k][j]

            b[i] = b[i] - m * b[k]  # untuk vektor b (yang dikanan sama dengan)

    return A, b
    # Yang menjadi masalah adalah ketika pivotnya itu 0, karena kalo pivotnya 0,
    # maka akan terjadi pembagian dengan 0 ketika mencari m


if __name__ == "__main__":
    A = np.array([
        [2, 3, -1],
        [4, 4, -3],
        [-2, 3, -1]
    ]) # pivotnya adalah [0,0] dan [1,1]

    b = np.array([5, 3, 1])
    N = 3

    x = np.zeros(N)
    A_segitiga, b_baru = naive_gauss_elimination(A, b, N)
    print(penyulihan_mundur(A_segitiga, b_baru, N, x))

