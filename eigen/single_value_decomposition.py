import numpy as np

from qr_decomposition import gram_schmidt


def svd_decomposition(A: np.ndarray) -> np.ndarray:
    aat = A @ A.T
    ata = A.T @ A
    y1 = np.linalg.eig(aat)[1]
    y2 = np.linalg.eig(ata)[1]

    U = gram_schmidt(y1, normalized=True)
    V = gram_schmidt(y2, normalized=True)
    S_diag = np.sqrt(np.linalg.eig(aat)[0])
    S = np.zeros(A.shape)
    for i in range(S_diag.shape[0]):
        S[i, i] = S_diag[i]

    return U, S, V


if __name__ == "__main__":
    A = np.array([
        [3, 1, 1],
        [-1, 3, 1],
    ])
    U, S, V = svd_decomposition(A)
    print(2/np.sqrt(6))
    print(V)
