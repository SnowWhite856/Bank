import mysql.connector
from tkinter import *

class MainMenu:
    def __init__(self):
        self.MainMenuWin = None

    def MainMenuWindow(self):
        self.MainMenuWin = Tk()
        
        self.MainMenuWin.geometry("250x400")



        self.MainMenuWin.mainloop()

