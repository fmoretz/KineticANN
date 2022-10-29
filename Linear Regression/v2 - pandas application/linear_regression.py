import torch
from torch import nn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os

# upload the data
dataset = pd.read_excel('dataset.xlsx')

# choose the parameter to identify
header = dataset.columns

for item in header:

    if item == 'HRT':
        pass
    else:
        u = item

        X_numpy = dataset['HRT'].to_numpy()
        Y_numpy = dataset[u].to_numpy()

        X = torch.from_numpy(X_numpy.astype(np.float32))
        y = torch.from_numpy(Y_numpy.astype(np.float32))

        X = X.view(X.shape[0], 1)
        y = y.view(y.shape[0], 1)

        n_samples, n_features = X.shape


        # build the model
        input_size = n_features
        output_size = 1

        model = nn.Sequential(
            nn.Linear(input_size,128),
            nn.Softplus(),
            nn.Linear(128, 128),
            nn.Softplus(),
            nn.Linear(128, 64),
            nn.Softplus(),
            nn.Linear(64, output_size)
        )

        loss = nn.MSELoss()
        optimizer = torch.optim.SGD(model.parameters(), lr = 1e-4)

        # train the model
        num_epochs = 5_000
        for epoch in range(num_epochs):
            prediction = model(X)
            l = loss(prediction, y)
            
            l.backward()
            optimizer.step()
            optimizer.zero_grad()
            
            if (epoch+1) % 100 == 0:
                print(f'epoch: {epoch+1} | loss: {l:>4f}')

        print('\nTraining finished!\n')
        predicted = model(X).detach().numpy()

        plt.figure(figsize=(5,4))

        plt.plot(X_numpy, Y_numpy, 'ko', label=u)
        plt.plot(X_numpy, predicted, 'r-', label='ANN pred.' )
        plt.legend()
        plt.xlabel('HRT')
        plt.ylabel(u)

# Save the model
torch.save(model.state_dict(), "provaADM1_all_param_regression_ANN.pth")
print("Saved PyTorch Model State to linear_regression_model.pth")

plt.show()

