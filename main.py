from grid import Grid

kRows = 20
kCols = 20

def main():
    useStartingFile = input('Would you like to use a starting file (y/n)? ').lower()[0]
    startingFile = ''
    
    # initialize grid and print grid to user
    cellGrid = None
    if useStartingFile == 'y':
        startingFile = input('Enter file name: ')
        cellGrid = Grid(kRows, kCols) # eventually replace with initialization from given file
        cellGrid.printGrid()
    else:
        rows = int(input('How many rows would you like the grid to have? '))
        cols = int(input('How many columns would you like the grid to have? '))
        cellGrid = Grid(rows, cols)
        cellGrid.printGrid()

        # get and format user input for starting cell
        startingCell = input('Which cell would you like to set on fire (row, col)? ')
        startingCell = startingCell.replace('(', '')
        startingCell = startingCell.replace(')', '')
        startingCell = startingCell.replace(',', '')

        # convert string of coordinates to ints
        startingCellCoordinates = startingCell.split(' ')
        startingCellRow = int(startingCellCoordinates[0])
        startingCellCol = int(startingCellCoordinates[1])

        # set starting cell on fire and print grid
        cellGrid.grid[startingCellRow - 1][startingCellCol - 1].status = 'burning'
        cellGrid.printGrid()

    # continue updating grid until user enters 0 as number of time steps to go forward
    timeSteps = int(input('How many time steps would you like to go forward? '))

    while True:
        if timeSteps == 0:
            break

        cellGrid.updateSteps(timeSteps)
        cellGrid.printGrid()

        timeSteps = int(input('How many time steps would you like to go forward? '))


if __name__ == '__main__':
    main()
