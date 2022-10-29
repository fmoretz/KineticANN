import torch
import torch.nn as nn
import numpy as np
from sklearn import datasets
from matplotlib import pyplot as plt

# data upload
x_numpy, y_numpy = datasets.make_regression(n_samples=100, n_features=1, noise=20)

# data preprocessing from numpy errors
X = torch.from_numpy(x_numpy.astype(np.float32))
y = torch.from_numpy(y_numpy.astype(np.float32))

# reshape
y = y.view(y.shape[0], 1)

n_sample, n_features = X.shape

# model definition
input_size = n_features
output_size = 1

model = nn.Linear(input_size, output_size)

# loss function
learning_rate = 0.1
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = learning_rate)

# training loop
num_epochs = 100
for epoch in range(num_epochs):
    
    prediction = model(X)
    loss = criterion(prediction, y)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    
    if (epoch + 1) % 10 == 0:
        print(f'epoch: {epoch + 1} | loss: {loss:>4f}')

print('\nTraining finished!\n')
print(f'weight found : {model.weight.data}')
print(f'bias found   : {model.bias.data}')
predicted = model(X).detach().numpy()

# Save the model
torch.save(model.state_dict(), "linear_regression_model.pth")
print("Saved PyTorch Model State to linear_regression_model.pth")

# # Load the model
# model = NeuralNetwork()
# model.load_state_dict(torch.load("model.pth"))

plt.figure()
plt.plot(x_numpy, y_numpy, 'ko')
plt.plot(x_numpy, predicted, 'b', linewidth=2)
plt.grid(True)
plt.show()