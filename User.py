class User:
    def __init__(self):
        self.id = 0
        self.username = None
        self.password = None
        self.email = None
        self.nrtel = None
        self.balance = 0
    
    def SetData(self, Data):
        self.id = Data[0]
        self.username = Data[1]
        self.password = Data[2]
        self.email = Data[3]
        self.nrtel = Data[4]
        self.balance = Data[5]
        print(str(self.id) + " " + self.username + " " + self.password + " " + self.email + " " + str(self.nrtel) + " " + str(self.balance))