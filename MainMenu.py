import mysql.connector
from tkinter import *

class MainMenu:
    def __init__(self, DataBase, User):
        self.MainMenuWin = None

        self.DataBase = DataBase
        self.User = User

    def MainMenuWindow(self):


        self.MainMenuWin = Tk()
        
        self.MainMenuWin.geometry("250x400")
        
        BalanceL = Label(self.MainMenuWin,
                        text=self.User.balance)
        BalanceL.pack()

        # HistoryB = Button(self.MainMenuWin,
        #                 command=self.History.HistoryWin)
        # HistoryB.pack()

        self.MainMenuWin.mainloop()

