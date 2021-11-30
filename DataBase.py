import mysql.connector

class DataBase:
    def __init__(self):
        self.host = "localhost"
        self.username = "root"
        self.password = ""
        self.bd = "banklogin"
        self.con = mysql.connector.connect(host=self.host, user=self.username, password=self.password, database=self.bd)
        self.cursor = self.con.cursor()
        self.sqlL = "SELECT username, password FROM dane WHERE username = %s AND password = %s"

    def Login(self, username, password):
        login = (username, password)
        self.cursor.execute(self.sqlL, login)
        result = self.cursor.fetchone()
        return result

    def Register(self, login, password, email, pyt, NrTel):
        pass

    def Historycheck(self):
        pass
