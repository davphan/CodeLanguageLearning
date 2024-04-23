import torch, torchvision
import numpy as np

# pretrained model, resnet18
model = torchvision.models.resnet18(pretrained=True)
# randomly simulated "image", 3 layers (rgb), 64x64
data = torch.rand(1, 3, 64, 64)
labels = torch.rand(1, 1000)

# forward pass
prediction = model(data)

# back pass
loss = (prediction - labels).sum() # error margin
loss.backwards()

# optimizer, learning rate = 0.01, momentum = 0.9
optim = torch.optim.SGD(model.paramters(), lr=1e-2, momentum=0.9)
optim.step() # gradient descent