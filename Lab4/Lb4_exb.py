
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

A = [[1, 2], [3, 4], [5, 6]]
B = [[7, 8, 9], [10, 11, 12]]

cA = len(A[0])
rB = len(B)
C = matMul(A, B, cA, rB)

print("New Matric C:")
for row in C:
    print(row)

