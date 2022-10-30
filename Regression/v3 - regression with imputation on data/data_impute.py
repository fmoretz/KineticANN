import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
import torch
from torch import nn
import numpy as np
import torchmetrics
from torchmetrics import R2Score
from torchsummary import summary
from torch.utils import data
from matplotlib import pyplot as plt

# load dataset
dataset = pd.read_excel('./v3 - regression with imputation on data/dataset.xlsx')

columns = dataset.columns

# impute dataset
imputer = KNNImputer(n_neighbors = 2, weights = 'distance')
dataset_imputed = imputer.fit_transform(dataset)

dataframe = pd.DataFrame(dataset_imputed, columns=columns)

# choose the columns on which do the learning
u = 'XT'

X_numpy = dataframe['HRT'].to_numpy()
Y_numpy = dataframe[u].to_numpy()

# split in train and test dataset
X_train, X_test, Y_train, Y_test = train_test_split(X_numpy, Y_numpy, test_size=0.3, shuffle=True, random_state=0)

X = torch.from_numpy(X_train.astype(np.float32))
y = torch.from_numpy(Y_train.astype(np.float32))
X = X.view(X.shape[0], 1)
y = y.view(y.shape[0], 1)

X_validation = torch.from_numpy(X_test.astype(np.float32))
y_validation = torch.from_numpy(Y_test.astype(np.float32))
X_validation = X_validation.view(X_validation.shape[0], 1)
y_validation = y_validation.view(y_validation.shape[0], 1)

n_samples, n_features = X.shape
n_nodes = 5

# build the model
model = nn.Sequential(
    nn.Linear(1, n_nodes),
    nn.Softplus(),
    nn.Linear(n_nodes, 1)
)

loss = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = 1e-3)

num_epochs = 20_000
store_loss = np.empty(num_epochs)

print(f'\n ===== Start training ===== \n')
model.train()
for epoch in range(num_epochs):
    prediction = model(X)
    eval_loss = loss(prediction, y)
    
    eval_loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    
    store_loss[epoch] = eval_loss
    
    if (epoch+1) % 500 == 0:
        print(f'epoch: {epoch+1} | loss: {eval_loss:>3f}')

# Summary print
print(f'\n ===== End training ===== \n')
for name, param in model.named_parameters():
    if param.requires_grad:
        print(f'Parameter : {name} = {param.data}\n')
print('\n',summary(model, X.shape),'\n')

# model test
model.eval()
with torch.no_grad():
    pred_val = model(X_validation)
    loss_val = loss(pred_val, y_validation)
r2score = R2Score()
print(f'Test loss: {loss_val:>3f} | Accuracy: {r2score(pred_val, y_validation):>3f} ')

# visualization
plt.figure(figsize=(5,4))
plt.plot(X_train, Y_train, 'ko', label='train data')
plt.plot(X_test, Y_test, 'bo', label='test data')

# scatter of prediction
X_val_numpy = X_validation.detach().numpy()
Y_val_numpy = pred_val.detach().numpy()
plt.plot(X_val_numpy, Y_val_numpy, 'rd', label='Prediction')

# model prediction on the entire set of data
X_total = torch.from_numpy(X_numpy.astype(np.float32))
X_total = X_total.view(X_total.shape[0], 1)

Y_prediction = model(X_total).detach().numpy()

plt.plot(X_total, Y_prediction, 'orange', label='ANN', linewidth=2)

# other settings
plt.xlabel('HRT')
plt.ylabel(u)
plt.grid(color='k', alpha=0.8, linestyle='dashed', linewidth=0.5)
plt.legend()
plt.show()