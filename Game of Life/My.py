
class Array2DNew:
    def __init__(self, numRows, numCols):
        self.grid = [[0]*numCols for _ in range(numRows)]
        self.numRows = numRows
        self.numCols = numCols

    def getElement(self, row, col):
        return self.grid[row][col]
    
    def setElement(self, row, col, value=1):
        self.grid[row][col] = value

    def clear(self, value):
        for i in range(self.numRows):
            for j in range(self.numCols):
                self.grid[i][j] = value

class LifeGridNew:
    LIVECELL = 1
    DEADCELL  = 0

    def __init__(self, numRows, numCols):
        self._grid = Array2DNew(numRows, numCols)
    
    def numRows(self):
        return self._grid.numRows
    
    def numCols(self):
        return self._grid.numCols

    def isLiveCell(self, row, col):
        return self._grid.getElement(row, col) == LifeGridNew.LIVECELL
    
    def clearCell(self, row, col):
        self._grid.setElement(row, col, LifeGridNew.DEADCELL)
    
    def setCell(self, row, col):
        self._grid.setElement(row, col)

    def configure(self, coordlist):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)

        for coord in coordlist:
            self.setCell(coord[0], coord[1])

    def numLiveNeighbours(self, row, col):
        count = 0
        for i in range(row-1, row + 2):
            for j in range(col-1, col+2):

                if i == row and j == col:
                    continue
                
                if (0 <= i < self.numRows()) and (0 <= j < self.numCols()):
                    if self.isLiveCell(i, j):
                        count += 1

        return count

class GameOfLife:
    def __init__(self, gen, width, height, coordList):
        self.gen = gen
        self.grid = LifeGridNew(width, height)
        self.grid.configure(coordList)
    
    def evolve(self):
        liveCells = list()

        for i in range(self.grid.numRows()):
            for j in range(self.grid.numCols()):

                neighbours = self.grid.numLiveNeighbours(i, j)

                if (neighbours == 2 and self.grid.isLiveCell(i, j)) or (neighbours == 3):
                    liveCells.append((i, j))

        self.grid.configure(liveCells)

    
    def draw(self):
        for i in range(self.grid.numRows()):
            for j in range(self.grid.numCols()):
                if self.grid.isLiveCell(i, j):
                    print("O", end = " ")
                
                else:
                    print(".", end=" ")
            print()

        print("-" * (2*self.grid.numCols()))

    
def main():
    init_config = [(1, 2), (2, 2), (3, 2)]
    grid = GameOfLife(3, 5, 5, init_config)

    print("Generation 0")
    grid.draw()
    for i in range(grid.gen):
        grid.evolve()
        print(f"Generation {i+1}")
        grid.draw()

if __name__ == "__main__":
    main()