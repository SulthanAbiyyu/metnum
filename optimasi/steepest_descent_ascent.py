import torch


# def steepest(f, x0, y0)


x = torch.tensor(2., requires_grad=True)
y = torch.tensor(1., requires_grad=True)

f = x ** 2 + y ** 2 + 2 * x + 4
f.backward()

print(x.grad())
