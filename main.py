from tkinter import *
from Sign_in import SignIn
from DataBase import DataBase
from MainMenu import MainMenu
from Sign_up import SignUp

DataBase = DataBase()
MainMenu = MainMenu()
SignUp = SignUp(DataBase)
SignIn = SignIn(DataBase, SignUp)

SignIn.SignInWindow()
if SignIn.result == 1:
    MainMenu.MainMenuWindow()