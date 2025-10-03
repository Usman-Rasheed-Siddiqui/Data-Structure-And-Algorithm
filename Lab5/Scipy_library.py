
import numpy
from scipy.sparse import diags

lower = [5, -7, 0]
middle = [1, 4, 3, 0]
upper = [9, -3, 6]

A_sparse = diags([lower, middle, upper], offsets=[-1, 0, 1], format = "csr")
print(A_sparse)

A_matrix = A_sparse.toarray()
print(A_matrix)