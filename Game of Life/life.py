from array1 import Array2D

class LifeGrid:
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, numRows, numCols):
        self._grid = Array2D(numRows, numCols)
        self.configure(list())

    def numRows(self):
        return self._grid.numRows()
    
    def numCols(self):
        return self._grid.numCols()
    
    def isLiveCell(self, row, col):
        return self._grid.get(row, col) == LifeGrid.LIVE_CELL

    def clearCell(self, row, col):
        self._grid.set(row, col, LifeGrid.DEAD_CELL)

    def setCell(self, row, col):
        self._grid.set(row, col, LifeGrid.LIVE_CELL)

    def configure(self, coordList):
        
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)

        for coord in coordList:
            self.setCell(coord[0], coord[1])


    def numLiveNeighbours(self, row, col):
        count = 0

        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i == row and j == col:
                    continue

                if (0 <= i < self.numRows()) and (0 <= j < self.numCols()):
                    if self.isLiveCell(i, j):
                        count += 1

        return count    



        