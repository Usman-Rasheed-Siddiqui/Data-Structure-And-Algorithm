
class Array2D:
    def __init__(self, numRows, numCols):
        self.grid = [[0]*numCols for _ in range(numRows)]
        self._numRows = numRows
        self._numCols = numCols

    def numRows(self):
        return self._numRows
    
    def numCols(self):
        return self._numCols
    
    def get(self, row, col):
        return self.grid[row][col]
    
    def set(self, row, col, value):
        self.grid[row][col] = value

    def clear(self, value):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self.grid[r][c] = value
    
    