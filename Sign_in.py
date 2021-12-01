from tkinter import *

class SignIn():
    def __init__(self, DataBase, SignUp, User):
        self.DataBase = DataBase
        self.User = User
        self.SignUp = SignUp
        self.result = None
        self.SignWin = Tk()

    def SignInWindow(self):
        self.SignWin

        self.SignWin.geometry("250x400")
        

        LUsername = Label(self.SignWin,
                        text="Username")
        LUsername.pack()

        EUsername = Entry(self.SignWin,
                        )
        EUsername.pack()

        LPassword = Label(self.SignWin,
                        text="Password")
        LPassword.pack()

        EPassword = Entry(self.SignWin,
                        )
        EPassword.pack()

        Login = Button(self.SignWin,
                        text="Login in",
                        command=lambda:self.SetLogin(EUsername.get(), EPassword.get()))
        Login.pack()

        SignUpB = Button(self.SignWin,
                        text="Don't have a account? Sing Up",
                        command=self.Registration)
        SignUpB.pack()

        self.SignWin.mainloop()

    def SetLogin(self, username, password):
        self.result = self.DataBase.Login(username, password)
        print(self.result)
        if self.result == 1:
            self.SignWin.destroy()

    def Registration(self):
        self.SignUp.SignUpWindow()