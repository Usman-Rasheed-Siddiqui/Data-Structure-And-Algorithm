
array = [23, 12, 1, 8, 34, 54, 2, 3]
n = len(array)
print("Before Sorting:", array)

def shell(num, n):
    k = int(n/2)

    while k > 0:
        for i in range(k, n):
            key = num[i]
            j = i
            while j >= k and num[j - k] > key:
                num[j] = num[j - k]
                j -= k
            num[j] = key
        k = int(k/2)

    return num

num = shell(array, n)
print("After Sorting:", num)


    