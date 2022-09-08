import numpy as np


def penyulihan_mundur(A, b, n, x):
    x[n-1] = b[n-1]/A[n-1][n-1]

    for k in range(n-2, -1, -1):
        sigma = 0
        for j in range(k+1, n):
            # x[j] itu nilai x yang udah didapeting sebelumnya, A[k][j] itu satu row atas dan kolom sama
            sigma = sigma + A[k][j] * x[j]
        # A[k][k] itu diagonal di row yang dicari
        x[k] = (b[k] - sigma) / A[k][k]

    return x


if __name__ == "__main__":
    A = np.array([
        [4, -1, 2, 3],
        [0, -2, 7, -4],
        [0, 0, 6, 5],
        [0, 0, 0, 3]
    ])
    b = np.array([20, -7, 4, 6])
    N = 4  # banyaknya variabel
    x = np.zeros(N)

    print(penyulihan_mundur(A, b, N, x))
