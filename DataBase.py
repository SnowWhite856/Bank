import mysql.connector

class DataBase:
    def __init__(self):
        self.host = "localhost"
        self.username = "root"
        self.password = ""
        self.bd = "banklogin"
        self.con = mysql.connector.connect(host=self.host, user=self.username, password=self.password, database=self.bd)
        self.cursor = self.con.cursor()

        #Login/Register
        self.sqlL = "SELECT username, password FROM dane WHERE username = %s AND password = %s"
        self.sqlR = "INSERT INTO dane(username, password, email, NrTel) VALUES (%s, %s, %s, %s)"

        #History
        self.sqlH = "SELECT * FROM history WHERE dane.id = history.id_dane"

    def Login(self, username, password):
        login = (username, password)
        self.cursor.execute(self.sqlL, login)
        result = self.cursor.fetchone()
        if result != None:
            return 1
        else:
            return 0

    def Register(self, username, password, email, NrTel):
        register = (username, password, email, NrTel)
        self.cursor.execute(self.sqlR, register)
        self.con.commit()

    def Historycheck(self):
        pass
