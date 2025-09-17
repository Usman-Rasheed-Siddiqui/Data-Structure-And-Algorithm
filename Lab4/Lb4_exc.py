
import numpy as np
from timeit import timeit

def matMul(A, B, cA, rB):

    if cA != rB:
        return "Column of A and Row of B do not match"

    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            C[i].append(0)

    for i in range(len(A)):
        for j in range(len(B[0])):
            C[i][j] = 0
            for k in range(len(A[0])):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]

    return C

def func1():

    A = [[1, 2], [3, 4], [5, 6]]
    B = [[7, 8, 9], [10, 11, 12]]

    cA = len(A[0])
    rB = len(B)
    matMul(A, B, cA, rB)

def func2():
    A = np.array([[1, 2], [3, 4], [5, 6]])
    B = np.array([[7, 8, 9], [10, 11, 12]])
    C = np.dot(A, B)

execution_matmul = timeit(func1, number=10000)
print(f"\nExecution time for matMul() function: {execution_matmul} seconds")

execution_np = timeit(func2, number=10000)
print(f"Execution time np.dot() function: {execution_np} seconds")

difference = execution_matmul - execution_np
print(f'Difference (User - Python): {difference} seconds')
