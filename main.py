import Tkinter as tk

# this class was originally taken from the online Tkinter reference document by John Shipman
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()


def main():
    app = Application()
    app.master.title('Sample Application')
    app.mainloop()


if __name__ == '__main__':
    main()

