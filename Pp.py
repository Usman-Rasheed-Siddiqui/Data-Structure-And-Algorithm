
class Array2d:
    def __init__(self, m, n):
        self.n = n
        self.m = m
        self.twodarray = self.make_array(n, m)


    def make_array(self, n, m):
        return [[0 for i in range(m)] for j in range(n)]
    
    def traverse_column(self):
        print("Traverse by columns:")
        for j in range(self.m):
            for i in range(self.n):
                print(self.twodarray[i][j], end = " ")
            print()

A = Array2d(3, 3)
A.twodarray = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

A.traverse_column()