
def STORETRIANGULAR(A, n):
    U = [0]*n
    i = 0
    for j in range(len(A)):
        for k in range(j+1):
            U[i] = A[j][k]
            i += 1

    return U

A = [[4, 0, 0, 0], [3, 5, 0, 0], [1, 6, 2, 0], [8, 0, 5, 9]]
length = len(A)
n = int((length/2)*(length+1))

U = STORETRIANGULAR(A, n)
print("Sparse Matrix:",U)

n = int((-1 + (1 + 8*(len(U)))**0.5)/2)

def RETRIEVETRIANGULAR(U, n):

    A = [[0 for i in range(n)] for i in range(n)]
    for j in range(n):
        for k in range(n):
            if k > j:
                A[j][k] = 0
            else:
                A[j][k] = U[int((j/2)*(j+1)) + k]

    return A

A = RETRIEVETRIANGULAR(U, n)
print("Original Triangular Matrix:")
for rows in A:
    print(rows)