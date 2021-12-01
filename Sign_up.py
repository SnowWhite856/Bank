from tkinter import *

class SignUp:
    def __init__(self, DataBase):
        self.SignUpWin = None
        self.DataBase = DataBase

    def SignUpWindow(self):
        self.SignUpWin = Tk()
        self.SignUpWin.geometry("250x400")

        UsernameL = Label(self.SignUpWin,
                        text="Username")
        UsernameL.pack()

        UsernameE = Entry(self.SignUpWin,
                        )
        UsernameE.pack()

        PasswordL = Label(self.SignUpWin,
                        text="Password")
        PasswordL.pack()

        PasswordE = Entry(self.SignUpWin,
                        )
        PasswordE.pack()

        EmailL = Label(self.SignUpWin,
                    text="Email")
        EmailL.pack()

        EmailE = Entry(self.SignUpWin,
                        )
        EmailE.pack()

        NrTelL = Label(self.SignUpWin,
                    text="Phone number")
        NrTelL.pack()

        NrTelE = Entry(self.SignUpWin,
                    )
        NrTelE.pack()

        Register = Button(self.SignUpWin,
                        command=lambda:self.Register(UsernameE.get(), PasswordE.get(), EmailE.get(), NrTelE.get()))
        Register.pack()

        Info = Label(self.SignUpWin)
        Info.pack()

        self.SignUpWin.mainloop()

    def Register(self, username, password, email, NrTel):
        self.DataBase.Register(username, password, email, NrTel)