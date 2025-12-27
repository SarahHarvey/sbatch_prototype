import torch
from torch.optim import SGD
import torch.nn as nn
import matplotlib.pyplot as plt

# Set device (GPU if available, else CPU)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Using device: {device}')

# Create a simple dataset
X = torch.randn(100, 10).to(device)
y = torch.randn(100, 1).to(device)

# Define the model
model = nn.Sequential(
    nn.Linear(10, 1),
    nn.ReLU(),
    # nn.Linear(64, 1)
).to(device)

# Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = SGD(model.parameters(), lr=0.01)

# Training loop
epochs = 1000
losses = []  # Track loss values

for epoch in range(epochs):
    # Forward pass
    outputs = model(X)
    loss = criterion(outputs, y)
    
    # Save loss
    losses.append(loss.item())
    
    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 20 == 0:
        print(f'Epoch {epoch + 1}/{epochs}, Loss: {loss.item():.4f}')

print("Training complete!")
