import Tkinter as tk

root = tk.Tk()
kRows = 50
kCols = 50
buttonGrid = []

def setupGUI():
    root.title('Wildfire Simulator')
    generateGrid(kRows, kCols)
    


def generateGrid(numRows, numCols):
    for r in range(0, numRows): 
        buttonGrid.append([])
        for c in range(0, numCols):
            button = tk.Button(root, command=lambda row=r, col=c: toggleCell(row, col), bg='green')
            button.grid(row=r, column=c)
            buttonGrid[r].append(button)


def toggleCell(row, col):
    pass


def main():
    pass


if __name__ == '__main__':
    main()

