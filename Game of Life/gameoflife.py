
from life import LifeGrid

init_config = [ (1, 1), (2, 2), (3, 2) ]

grid_width = 5
grid_height = 5

num_gens = 8

def main():
    grid = LifeGrid(grid_width, grid_height)
    grid.configure(init_config)

    draw(grid)

    for i in range(num_gens):
        evolve(grid)
        draw(grid)

    
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
                print("O", end = " ")
            else:
                print(".", end = " ")

        print()
    
    print("-" * (2*grid.numCols()))


if __name__ == "__main__":
    main()