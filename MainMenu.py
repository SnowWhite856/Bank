import mysql.connector
from tkinter import *

class MainMenu:
    def __init__(self, History):
        self.MainMenuWin = None
        self.History = History
        self.Balance = None

    def MainMenuWindow(self):
        

        self.MainMenuWin = Tk()
        
        self.MainMenuWin.geometry("250x400")
        
        BalanceL = Label(self.MainMenuWin,
                        text=self.Balance)
        BalanceL.pack()

        HistoryB = Button(self.MainMenuWin,
                        command=self.History.HistoryWin)
        HistoryB.pack()

        self.MainMenuWin.mainloop()

