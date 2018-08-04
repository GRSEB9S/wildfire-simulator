from cell import Cell
from copy import deepcopy

class Grid:
    def __init__(self, rows, cols):
        self.grid = []
        self.rows = rows
        self.cols = cols

        for r in range(rows):
            self.grid.append([])  
            for c in range(cols):
                # change initialization to take in data from csv file
                self.grid[r].append(Cell('unburned', 1, 0, 0, 0, 1))


    def updateSteps(self, timeSteps):
        for i in range(timeSteps):
            self.update()


    def update(self):
        # make a copy of the grid, not a reference to it
        tempGrid = deepcopy(self.grid)

        for r in range(self.rows):
            for c in range(self.cols):
                tempGrid[r][c].status = self.stateFunction(r, c)

        self.grid = tempGrid


    def stateFunction(self, row, col):
        status = self.grid[row][col].status

        # do calculations
        # change status appropriately
        if status == 'unburned':
            # check if surrounding cells are burning; if so, spread fire to current cell
            for i in range(-1, 2):
                for j in range(-1, 2):
                    isInBounds = ((row + i) >= 0 and (row + i) < self.rows) and ((col + j) >= 0 and (col + j) < self.cols)
                    if isInBounds and self.grid[row + i][col + j].status == 'burning':
                        status = 'burning'
        elif status == 'burning':
            status = 'burned'
        
        return status


    def printGrid(self):
        for r in range(self.rows):
            print()  # newline

            for c in range(self.cols):
                self.grid[r][c].printCell()
                print('   ', end='')  # spacing between cells

        print('\n')  # 2 newlines

