from tkinter import *
from Sign_in import SignIn
from DataBase import DataBase
from MainMenu import MainMenu
from Sign_up import SignUp
from History import History
from User import User


User = User()
DataBase = DataBase(User)
MainMenu = MainMenu(DataBase, User)
SignUp = SignUp(DataBase)
SignIn = SignIn(DataBase, SignUp, User)
History = History(DataBase, User)

SignIn.SignInWindow()
if SignIn.result == 1:
    MainMenu.MainMenuWindow()