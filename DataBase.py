import mysql.connector

class DataBase:
    def __init__(self, User):
        self.host = "localhost"
        self.username = "root"
        self.password = ""
        self.bd = "banklogin"
        self.con = mysql.connector.connect(host=self.host, user=self.username, password=self.password, database=self.bd)
        self.cursor = self.con.cursor()

        self.User = User

        #Login/Register
        self.sqlL = "SELECT * FROM dane WHERE username = %s AND password = %s"
        self.sqlR = "INSERT INTO dane(username, password, email, NrTel) VALUES (%s, %s, %s, %s)"

        #Menu
        self.sqlB = "SELECT balance FROM dane WHERE %s"

        #History
        self.sqlHS = "SELECT * FROM history WHERE dane.id = history.id_dane AND dane.id = %s"

        #Transfer
        self.sqlC = "UPDATE dane SET balance = %s WHERE dane.username = %s" 
        self.sqlCT = "SELECT balance FROM dane WHERE username = %s"

    def Login(self, username, password):
        login = (username, password)
        self.cursor.execute(self.sqlL, login)
        result = self.cursor.fetchone()
        if result != None:
            self.User.SetData(result)
            return 1
        else:
            return 0

    def Register(self, username, password, email, NrTel):
        register = (username, password, email, NrTel)
        self.cursor.execute(self.sqlR, register)
        self.con.commit()

    def Transfer(self, UserF, UserT, Hm):
        print(self.User.balance)
        print(type(self.User.balance))
        UserT = (UserT, )
        balanceT = self.cursor.execute(self.sqlCT, UserT)

        balance = int(self.User.balance) - int(Hm)
        print(balance)

        FChange = (UserF, balance)
        TChange = (UserT, (int(balanceT)+int(Hm)))
        self.cursor.execute(self.sqlC, FChange)
        self.cursor.execute(self.sqlC, TChange)

    def HistoryShow(self, Hlist):
        result = self.cursor.execute(self.sqlHS)
        for item in result:
            Hlist.append(item[0])
        return result

    def HistorySelect(self, Selection):
        if Selection != None:
            select = (Selection, )
            result = self.cursor.execute(self.sqlHS, select)
            return result
                

