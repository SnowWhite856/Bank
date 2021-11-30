from tkinter import *
from Sign_in import SignIn
from DataBase import DataBase
from MainMenu import MainMenu

DataBase = DataBase()
MainMenu = MainMenu()
SignIn = SignIn(DataBase)

SignIn.SignInWindow()
MainMenu.MainMenuWindow()