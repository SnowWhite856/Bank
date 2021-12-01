class User:
    def __init__(self):
        self.id = None
        self.username = None
        self.password = None
        self.email = None
        self.nrtel = None
        self.balance = None
    
    def SetData(self, Data):
        self.id = Data[0]
        self.username = Data[1]
        self.password = Data[2]
        self.email = Data[3]
        self.nrtel = Data[5]
        self.balance = Data[6]
        print(str(self.id) + " " + self.username + " " + self.password + " " + self.email + " " + str(self.nrtel) + " " + str(self.balance))