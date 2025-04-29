import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

# Compute exp(x) for each element
exps = np.exp(x)

# Normalize so that the total sum is 1
softmax = exps / np.sum(exps)

plt.plot(x, 1 / (1 + np.exp(-x)), label='Sigmoid')
plt.plot(x, np.tanh(x), label='tanh')
plt.plot(x, np.maximum(0, x), label='ReLU')
plt.plot(x, x, label='Identity')
plt.plot(x, softmax, label='Softmax')

plt.xlabel('Input')
plt.ylabel('Activation')
plt.title('Activation Functions')
plt.legend()
plt.grid(True)
plt.show()