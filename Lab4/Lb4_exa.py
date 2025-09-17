
# Matrix Multiplication

def matMul(A, B, n):
    C = []
    for i in range(n):
        C.append([])
        for j in range(n):
            C[i].append(0)

    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]

    return C

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
n = len(A)
C = matMul(A, B, n)

print("New Matric C:")
for row in C:
    print(row)





