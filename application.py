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
            button = tk.Button(root, bg='green')
            button.grid(row=r, column=c, sticky=tk.N+tk.S+tk.E+tk.W)
            buttonGrid[r].append(button)
 
            button.bind('<Button-1>', lambda click=1: toggleCell(r, c, click)) 
            button.bind('<Button-3>', lambda click=3: toggleCell(r, c, click)) 

            root.rowconfigure(r, weight=1)
            root.columnconfigure(c, weight=1)


def toggleCell(row, col, click):
    if click == 1: 
        buttonGrid[int(row)][int(col)].config(bg='red')
    elif click == 3:
        buttonGrid[int(row)][int(col)].config(bg='black')


