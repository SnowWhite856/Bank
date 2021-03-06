from tkinter import *
from Sign_in import SignIn
from DataBase import DataBase
from MainMenu import MainMenu
from Sign_up import SignUp
from History import History
from User import User
from Transfer import Transfer


User = User()
DataBase = DataBase(User)
SignUp = SignUp(DataBase)
SignIn = SignIn(DataBase, SignUp, User)
History = History(DataBase, User)
Transfer = Transfer(DataBase, User)
MainMenu = MainMenu(DataBase, User, History, Transfer)

SignIn.SignInWindow()
if SignIn.result == 1:
    MainMenu.MainMenuWindow()