from tkinter import *

class History:
    def __init__(self, DataBase, User):
        self.HistoryWin = None

        self.User = User
        self.DataBase = DataBase
        self.Hadata = None
    
    def SetHistoryWin(self):
        self.HistoryWin = Tk()
        self.HistoryWin.geometry("250x400")

        list = Listbox(self.HistoryWin,
                        )
        list.pack()

        Data = Label(self.HistoryWin,
                    text = self.DataBase.HistorySelect(list.curselection()))
        Data.pack()

        self.Hdata = self.DataBase.HistoryShow(list)

        self.HistoryWin.mainloop()