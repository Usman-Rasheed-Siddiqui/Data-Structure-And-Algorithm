
class Array2D:
    def __init__(self, numRows, numCols):
        self.grid = [[0]*numCols for _ in range(numRows)]
    
    def get(self, row, col):
        return self.grid[row][col]
    
    def set(self, row, col):
        self.grid[row][col]

    def clear(self, value):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self.grid[r][c] = value
    
    