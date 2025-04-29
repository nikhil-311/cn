import numpy as np
import matplotlib.pyplot as plt

# Define activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

# Create input range
x = np.linspace(-10, 10, 400)

# Compute outputs
y_sigmoid = sigmoid(x)
y_tanh = tanh(x)
y_relu = relu(x)

# Plot
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Sigmoid
axes[0].plot(x, y_sigmoid, color='blue')
axes[0].set_title('Sigmoid Activation')
axes[0].grid(True)

# Tanh
axes[1].plot(x, y_tanh, color='green')
axes[1].set_title('Tanh Activation')
axes[1].grid(True)

# ReLU
axes[2].plot(x, y_relu, color='red')
axes[2].set_title('ReLU Activation')
axes[2].grid(True)

# General figure title
fig.suptitle('Comparison of Sigmoid, Tanh, and ReLU', fontsize=16)
plt.show()