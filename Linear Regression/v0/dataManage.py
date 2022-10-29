import torch
def loadArray(array, batch_size, train=True):
	from torch.utils import data
	
	dataset = data.TensorDataset(*array)

	return data.DataLoader(dataset, batch_size, shuffle=train)

def reshaper(X, y):	
	return X.reshape((-1, 1)), y.reshape((-1, 1))


def train(dataloader, model, loss_fn, optimizer):
	import torch
	size = len(dataloader.dataset)
	model.train()
	
	device = 'cpu'
	
	# use cross entropy
	for batch, (X, y) in enumerate(dataloader):
		X, y = X.to(device), y.to(device)

		# compute prediction error
		pred = model(X)
		loss = loss_fn(pred, y)

		# backpropagation
		optimizer.zero_grad() # try to zero the gradient descent
		loss.backward() # go back proceeding the optimization to other parameters behind
		optimizer.step() # do

		# print
		if batch % 10 == 0:
			loss, current = loss.item(), batch * len(X)
			print(f'loss: {loss:>7} [{current:>5d}/{size:>5d}]')

def test(dataloader, model, loss_fn): 
	size = len(dataloader.dataset)
	num_batches = len(dataloader)
	
	# model results evaluation
	model.eval()
	
	# initialization
	test_loss, correct = 0, 0
	with torch.no_grad(): # deactivate gradient descent
		for X, y in dataloader:
			pred = model(X)
			test_loss += loss_fn(pred, y).item()
			correct += (pred.argmax(1) == y).type(torch.float).sum().item()
		test_loss /= num_batches
		correct /= size
	print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")