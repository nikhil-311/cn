import numpy as np

def fuzzy_union(A, B):
    return np.maximum(A, B)

def fuzzy_intersection(A, B):
    return np.minimum(A, B)

def fuzzy_complement(A):
    return 1 - A

def fuzzy_difference(A, B):
    return np.maximum(A, 1 - B)

def cartesian_product(A, B):
    return np.outer(A, B)

def max_min_composition(R, S):
    return np.max(np.minimum.outer(R, S), axis=1)

A = np.array([0.2, 0.4, 0.6, 0.8])
B = np.array([0.3, 0.5, 0.7, 0.9])

union_result = fuzzy_union(A, B)
intersection_result = fuzzy_intersection(A, B)
complement_A = fuzzy_complement(A)
difference_result = fuzzy_difference(A, B)

print("Union:", union_result)
print("Intersection:", intersection_result)
print("Complement of A:", complement_A)
print("Difference:", difference_result)

R = np.array([0.2, 0.5, 0.4])
S = np.array([0.6, 0.3, 0.7])

cartesian_result = cartesian_product(R, S)
composition_result = max_min_composition(R, S)

print("Cartesian product of R and S:")
print(cartesian_result)

print("Max-Min composition of R and S:")
print(composition_result)