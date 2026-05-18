import numpy as np

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate Synthetic Structural Damage Data
X, y = make_classification(
    n_samples=500,
    n_features=10,
    n_classes=2,
    random_state=42
)

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2
)

# AIS Classifier
class AISClassifier:

    def __init__(self,
                 num_antibodies=20,
                 clone_factor=10,
                 mutation_rate=0.1):

        self.num_antibodies = num_antibodies
        self.clone_factor = clone_factor
        self.mutation_rate = mutation_rate

    # Initialize antibodies
    def initialize_antibodies(self, X, y):

        indices = np.random.choice(len(X), self.num_antibodies)

        self.antibodies = X[indices]
        self.labels = y[indices]

    # Affinity function
    def affinity(self, antibody, antigen):

        return -np.linalg.norm(antibody - antigen)

    # Clone and mutate antibodies
    def clone_and_mutate(self):

        clones = []
        labels = []

        for i, ab in enumerate(self.antibodies):

            for _ in range(self.clone_factor):

                clone = ab + self.mutation_rate * np.random.randn(*ab.shape)

                clones.append(clone)
                labels.append(self.labels[i])

        return np.array(clones), np.array(labels)

    # Selection process
    def select(self, X, y, clones, clone_labels):

        combined_X = np.vstack((self.antibodies, clones))
        combined_y = np.hstack((self.labels, clone_labels))

        fitness = []

        for ab, label in zip(combined_X, combined_y):

            score = 0

            for xi, yi in zip(X, y):

                if self.predict_one(xi, ab, label) == yi:
                    score += 1

            fitness.append(score)

        idx = np.argsort(fitness)[-self.num_antibodies:]

        self.antibodies = combined_X[idx]
        self.labels = combined_y[idx]

    # Predict single sample
    def predict_one(self, x, antibody=None, label=None):

        if antibody is not None:
            return label

        distances = [np.linalg.norm(x - ab)
                     for ab in self.antibodies]

        idx = np.argmin(distances)

        return self.labels[idx]

    # Train model
    def fit(self, X, y, generations=10):

        self.initialize_antibodies(X, y)

        for _ in range(generations):

            clones, clone_labels = self.clone_and_mutate()

            self.select(X, y, clones, clone_labels)

    # Predict all samples
    def predict(self, X):

        return np.array([self.predict_one(x) for x in X])

# Train and evaluate model
model = AISClassifier()

model.fit(X_train, y_train)

preds = model.predict(X_test)

accuracy = accuracy_score(y_test, preds)

print("Accuracy:", accuracy)