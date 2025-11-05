
class Array2D:
    def __init__(self, numRows, numCols):
        self._grid = [[0]*numCols for _ in range(numRows)]
        self._numRows = numRows
        self._numCols = numCols

    def numRows(self):
        return self._numRows
    
    def numCols(self):
        return self._numCols
    
    def set(self, row, col, value):
        self._grid[row][col] = value
    
    def get(self, row, col):
        return self._grid[row][col]
    
    def clear(self, value):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.set(i, j, value)


class LifeGrid:
    LiveCell = 1
    DeadCell = 0
    def __init__(self, numRows, numCols):
        self._grid = Array2D(numRows, numCols)
        self.configure(list())
    
    def numRows(self):
        return self._grid.numRows()

    def numCols(self):
        return self._grid.numCols()

    def setCell(self, row, col):
        self._grid.set(row, col, LifeGrid.LiveCell)

    def clearCell(self, row, col):
        self._grid.set(row, col, LifeGrid.DeadCell)

    def isLiveCell(self, row, col):
        return self._grid.get(row, col) == LifeGrid.LiveCell
    
    def configure(self, coordlist):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)

        for coord in coordlist:
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

def evolve(grid):
    liveCells = list()

    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            neighbours = grid.numLiveNeighbours(i, j)

            if (neighbours == 2 and grid.isLiveCell(i, j)) or (neighbours == 3):
                liveCells.append((i, j))

    grid.configure(liveCells)

def draw(grid):
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            if grid.isLiveCell(i, j):
                print("O", end=" ")
            else:
                print(".", end = " ")
        print()

    print("- "*grid.numCols())


def main():
    gridHeight = int(input("Enter height for the grid: "))
    gridWidth = int(input("Enter width for the grid: "))
    
    gen = int(input("Enter number of generations: "))

    grid = LifeGrid(gridWidth, gridHeight)
    grid.configure([(1, 2), (2, 1), (2, 2), (2, 3)])

    draw(grid)
    for i in range(gen):
        evolve(grid)
        draw(grid)

if __name__ == "__main__":
    main()