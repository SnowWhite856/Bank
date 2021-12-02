import mysql.connector
from tkinter import *

class MainMenu:
    def __init__(self, DataBase, User, History):
        self.MainMenuWin = None

        self.DataBase = DataBase
        self.User = User
        self.History = History

    def MainMenuWindow(self):


        self.MainMenuWin = Tk()
        
        self.MainMenuWin.geometry("250x400")
        
        BalanceL = Label(self.MainMenuWin,
                        text=self.User.balance)
        BalanceL.pack()

        HistoryB = Button(self.MainMenuWin,
                        command=self.OpenHistory)
        HistoryB.pack()

        self.MainMenuWin.mainloop()

    def OpenHistory(self):
        self.MainMenuWin.destroy()
        self.History.HistoryWin()

