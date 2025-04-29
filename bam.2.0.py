import numpy as np

def sign(x):
    """Custom sign function: +1 if >=0, else -1"""
    return np.where(x >= 0, 1, -1)

def train_bam(X, Y):
    """Train BAM by outer products"""
    W = np.dot(X.T, Y)
    return W

def full_bidirectional_recall(W, init_x=None, init_y=None, max_iters=10):
    """Recall (x,y) pair by alternating until convergence"""
    x = init_x.copy() if init_x is not None else None
    y = init_y.copy() if init_y is not None else None

    for iteration in range(max_iters):
        prev_x = x.copy() if x is not None else None
        prev_y = y.copy() if y is not None else None
        
        # Step 1: if x known, update y
        if x is not None:
            y = sign(np.dot(W.T, x))
        
        # Step 2: if y known, update x
        if y is not None:
            x = sign(np.dot(W, y))

        # Check for convergence
        if np.array_equal(x, prev_x) and np.array_equal(y, prev_y):
            print(f"Converged in {iteration+1} iterations.")
            break

    return x, y

# Example usage

# Training patterns
X = np.array([
    [1, -1],
    [-1, 1]
])

Y = np.array([
    [1, -1],
    [-1, 1]
])

# Train BAM
W = train_bam(X, Y)

# Start with a noisy x pattern
init_x = np.array([1, -1])

# Perform full bidirectional recall
final_x, final_y = full_bidirectional_recall(W, init_x=init_x)

print("Final x:", final_x)
print("Final y:", final_y)