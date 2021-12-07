import mysql.connector
from tkinter import *

class MainMenu:
    def __init__(self, DataBase, User, History, Transfer):
        self.MainMenuWin = None

        self.DataBase = DataBase
        self.User = User
        self.History = History
        self.Transfer = Transfer

    def MainMenuWindow(self):
        self.MainMenuWin = Tk()
        
        self.MainMenuWin.geometry("250x400")
        
        BalanceL = Label(self.MainMenuWin,
                        text=self.User.balance)
        BalanceL.pack()

        TransferB = Button(self.MainMenuWin,
                            text="Transfer",
                            command=self.Transfer.TransferWindow)
        TransferB.pack()

        HistoryB = Button(self.MainMenuWin,
                        text="History",
                        command=self.OpenHistory)
        HistoryB.pack()

        self.MainMenuWin.mainloop()

    def OpenHistory(self):
        self.MainMenuWin.destroy()
        self.History.HistoryWin()

