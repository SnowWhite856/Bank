import mysql.connector
from tkinter import *

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
        self.sqlC = "UPDATE dane SET balance = %s WHERE id = %s" 
        self.sqlCT = "SELECT balance FROM dane WHERE id = %s"

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

    def Transfer(self, UserT, Hm):
        if Hm != None or Hm != 0: 
            print(self.User.balance)
            print(type(self.User.balance))
            UserT = (UserT, )
            self.cursor.execute(self.sqlCT, UserT)

            balanceT = self.cursor.fetchone()

            balanceT = balanceT[0]

            balance = int(self.User.balance) - int(Hm)

            balanceT = balanceT + int(Hm)
            
            FChange = (balance, self.User.id)
            TChange = (balanceT, UserT[0])
            self.cursor.execute(self.sqlC, FChange)
            self.con.commit()
            self.cursor.execute(self.sqlC, TChange)
            self.con.commit()

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
                

