from tkinter import *

class SignIn():
    def __init__(self, DataBase):
        self.username = ""
        self.password = ""
        self.DataBase = DataBase
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

        SignUp = Button(self.SignWin,
                        text="Don't have a account? Sing Up")
        SignUp.pack()

        self.SignWin.mainloop()

    def SetLogin(self, username, password):
        self.username = username
        self.password = password
        self.result = self.DataBase.Login(self.username, self.password)
        print(self.result)
        if self.result == (username, password):
            self.SignWin.destroy()