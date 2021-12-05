from tkinter import *

class Transfer:
    def __init__(self, DataBase, User):
        self.window = None
        self.DataBase = DataBase
        self.User = User
        
    def TransferWindow(self):
        self.window = Tk()

        UserFL = Label(self.window,
                        text="Your account")
        UserFL.pack()

        UserFE = Label(self.window,
                        text=self.User.id)
        UserFE.pack()

        UserTL = Label(self.window,
                        text="Account to send money")
        UserTL.pack()

        UserTE = Entry(self.window,
                        )
        UserTE.pack()

        HmL = Label(self.window,
                    text="How much do you want to send money?")
        HmL.pack()

        HmE = Entry(self.window,
                    )
        HmE.pack()

        Send = Button(self.window,
                        text="Send",
                        command=lambda:self.DataBase.Transfer(UserTE.get(), HmE.get()))
        Send.pack()

        self.window.mainloop()