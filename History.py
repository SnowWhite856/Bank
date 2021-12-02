from tkinter import *

class History:
    def __init__(self, DataBase, User):
        self.HistoryWin = None

        self.User = User
        self.DataBase = DataBase
    
    def SetHistoryWin(self):
        self.HistoryWin = Tk()
        self.HistoryWin.geometry("250x400")


        self.HistoryWin.mainloop()