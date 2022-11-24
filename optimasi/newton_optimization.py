import torch


def newton_optimization(fx: torch.tensor, x0: torch.tensor, n_iter: int = 1):

    for _ in range(n_iter):
        fx.backward(create_graph=True)
        first = x0.grad.clone()
        x0.grad.data.zero_()
        x0.grad.backward()
        second = x0.grad.clone()

        x0 = x0 - (first / second)

    return x0


if __name__ == "__main__":
    x = torch.tensor(2.5, requires_grad=True)
    g = 2 * torch.sin(x) - (x ** 2 / 10)

    newton_optimization(g, x, n_iter=1)
