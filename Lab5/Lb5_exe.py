def RETRIEVETRIDIAGONAL(U, n):
    B = [[0 for i in range(n)] for i in range(n)]

    l = 0
    for j in range(n):
        for k in range(n):
            if abs(j - k) <= 1:
                B[j][k] = U[2*j + k]
            
            else:
                B[j][k] = 0

    return B

U = [5, -7, 1, 4, 3, 9, -3, 6, 2, 4]
n = int((len(U) + 2)/3)

B = RETRIEVETRIDIAGONAL(U, n)
print("Tridiagonal Matrix:",B)

