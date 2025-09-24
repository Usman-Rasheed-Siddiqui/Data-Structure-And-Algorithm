

B = [[5, -7, 0, 0], [1, 4, 3, 0], [0, 9, -3, 6], [0, 0, 2, 4]]
n = 3*(len(B)) - 2

def STORETRIDIAGONAL(B, n):
    U = [0]*n

    i = 0
    for j in range(len(B)):
        for k in range(len(B)):
            if abs(j - k) <= 1:
                U[i] = B[j][k]
                i += 1
            else:
                U[i] = 0
    return U
U = STORETRIDIAGONAL(B, n)

n = int((len(U) + 2)/3)

def RETRIEVETRIDIAGONAL(U, n):
    B = [[0 for i in range(n)] for i in range(n)]
    print(B)

    for j in range(n):
        for k in range(n):
            if abs(j - k) <= 1:
                B[j][k] = U[(3*j + k)]
                print(B[j][k])
                print(B)
            else:
                B[j][k] = 0

    return B

B = RETRIEVETRIDIAGONAL(U, n)
print(B)