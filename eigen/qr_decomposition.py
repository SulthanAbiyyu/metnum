import numpy as np

def gram_schmidt(A: np.ndarray, normalized=True) -> np.ndarray:
    V = np.zeros(A.shape)
    V[:, 0] = A[:, 0]

    for col in range(1, A.shape[1]):
        summa = 0
        for w in range(col):
            summa += (A[:, col] @ V[:, w]) / np.linalg.norm(V[:, w]) * V[:, w]
        V[:, col] = A[:, col] - summa
    
    if normalized:
        for col in range(V.shape[1]):
            V[:, col] = V[:, col] / np.linalg.norm(V[:, col] ** 2)
    
    return V

if __name__ == "__main__":
    A = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    V = gram_schmidt(A)

    print(np.linalg.norm(V[:, 0]))