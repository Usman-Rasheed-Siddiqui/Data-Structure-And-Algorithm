
import numpy as np
from scipy.sparse import csr_matrix

# 3 x 6 array
dense_array = np.array([
    [1, 0, 0, 0, 2, 0],
    [0, 0, 3, 0, 0, 0],
    [4, 0, 0, 5, 0, 6]
])

csr = csr_matrix(dense_array)
print("CSR Representation:")
print(csr)
print("Data:", csr.data)
print("Indices:", csr.indices)
print("Indptr:", csr.indptr)

array_back = csr.toarray()
print("Converted to Dense Array:\n",array_back)
