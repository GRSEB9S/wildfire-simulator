from cell import Cell

class Grid:
    def __init__(self, rows, cols):
        self.grid = []
        self.rows = rows
        self.cols = cols

        for r in range(rows):
            self.grid.append([])  
            for c in range(cols):
                self.grid[r].append(Cell('unburned', 1, 0, 0, 0, 1))


    def update(self, timeSteps):
        for i in range(timeSteps):
            update()


    def update(self):
        for r in range(self.rows):
            for c in range(self.cols):
                pass


    def printGrid(self):
        for r in range(self.rows):
            print       # newline
            for c in range(self.cols):
                self.grid[r][c].printCell()
                print ' ',
