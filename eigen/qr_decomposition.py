import numpy as np


def gram_schmidt(A: np.ndarray, normalized=True) -> np.ndarray:
    V = np.zeros(A.shape)
    V[:, 0] = A[:, 0]

    for col in range(1, A.shape[1]):
        summa = 0
        for w in range(col):
            summa += (A[:, col] @ V[:, w]) / \
                (np.linalg.norm(V[:, w]) ** 2) * V[:, w]
        V[:, col] = A[:, col] - summa

    if normalized:
        for col in range(V.shape[1]):
            V[:, col] = V[:, col] / np.linalg.norm(V[:, col])

    return V


def qr_decompose(A, normalized=True):
    Q = gram_schmidt(A, normalized)
    R = Q.T @ A

    return Q, R


def qr_eigen_iteration(A, n_iter=100, normalized=True):
    Q, R = qr_decompose(A, normalized)
    A_baru = np.zeros(A.shape)
    for _ in range(n_iter):
        A_baru = R @ Q
        Q, R = qr_decompose(A_baru)

    return A_baru


if __name__ == "__main__":
    A = np.array([
        [2, 1, 2],
        [1, 3, 4],
        [2, 2, 1]
    ])
    q, r = qr_decompose(A)
    print(q)
    print(r)
    # print(qr_eigen_iteration(A))
