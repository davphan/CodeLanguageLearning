import torch

# tensors
x = torch.tensor([2.5, 0.1])
y = torch.tensor([3.0, 2.4])
print(y.add(x))

# autograd
x = torch.randn(3, requires_grad=True)
# gradient function stored!!!
print(x)
# forward prop, gradient function can be used to back prop
y = x + 2
print(y)
# forward prop, another grad_func stored with "z"
z = y * y * 2
# z = z.mean()
print(z)

v = torch.tensor([0.1, 1.0, 0.001], dtype=torch.float32)
# gradient of z with respect to x, dz/dx
z.backward(v) # if z is not a scalar, needs an argument of the same size (vector jacobian product)
print(x.grad)

# prevent tracking gradient
# x.requires_grad_(False)
# x.detach()
# with torch.no_grad():

# i.e.
weights = torch.ones(4, requires_grad=True)
for epoch in range(3):
  model_output = (weights*3).sum()

  model_output.backward()

  print(weights.grad)

  weights.grad.zero_() # reset gradient on each loop!

optimizer = torch.optim.SGD(weights, lr=0.01)


# Back Propagation
