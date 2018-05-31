import Tkinter as tk

class GUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self): 
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

    def updateGrid(self, grid):
        pass
        
