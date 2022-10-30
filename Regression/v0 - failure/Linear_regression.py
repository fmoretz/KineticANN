import torch
from torch import nn
from torch.utils import data
from matplotlib import pyplot as plt
import numpy as np
from dataManage import *
from sklearn.model_selection import train_test_split

data_length = 8000

# initialize random seed and matrix
A = torch.normal(0, 1, (data_length, 1))
noise = torch.normal(0, 0.1, A.shape)

# initialize 'true' values for m and q
m = torch.tensor([1.2])
q = torch.tensor(0.6)

y_t = torch.matmul(A, m) + q + noise


# load data to dataset
batch = 10 # simple batch size
features, labels = A, y_t
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, shuffle=True)

# iterable of the dataset
data = loadArray(array=(features, labels), batch_size=batch)
data_train = loadArray((x_train, y_train), batch)
data_test = loadArray((x_test, y_test), batch)

# obtain data from the data iterable
next(iter(data))

# model definition
neural_net = nn.Linear(1, 1) # one single transformation

# weigth and bias initialization
neural_net.weight.data.normal_(0, 2)
neural_net.bias.data.fill_(0)

# define loss function
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(neural_net.parameters(), lr=1e-7)

print(f'Raw prediction (before training:')
print(f'm used: {neural_net.weight.data}')
print(f'q used: {neural_net.bias.data}')  
print(f'X shape: {features.shape}')
print(f'y shape: {labels.shape}')

num_epochs = 70
for t in range(num_epochs): 
    # for batch, (X, y) in enumerate(data, 0):
    #     l = loss_fn(neural_net(X) ,y)
    #     optimizer.zero_grad() #sets gradients to zero
    #     l.backward() # back propagation
    #     optimizer.step() # parameter update
    #     l = loss_fn(neural_net(features), labels)
    #     print(f'batch: {batch} | epoch {epoch + 1} | Loss {l:f}')
    
    print(f"Epoch {t+1}\n-------------------------------")
    train(data_train, neural_net, loss_fn, optimizer)

# get final parameters after training
m_final = neural_net.weight.data
q_final = neural_net.bias.data

neural_net.eval()
for batch, (X, y) in enumerate(data_test):
    pred = neural_net(X)

print('\nTraining finished!\n')
print(f'predicted m: {m_final}')
print(f'predicted q: {q_final}')
print('error in estimating m:', m - m_final.reshape(m.shape))
print('error in estimating c:', q_final - q)
    
plt.figure(figsize=(5,5))
plt.plot(A, m*A + q + noise, 'ko')
plt.plot(A, m_final*A + q_final, 'b-')

plt.ylabel('labels')
plt.xlabel('feutures')
plt.grid(True)
plt.show()