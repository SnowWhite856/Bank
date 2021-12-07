import mysql.connector
from tkinter import *
import datetime

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
        self.sqlAH = "INSERT INTO history(Ufrom, Uto, date, hm) VALUES (%s, %s, %s, %s)"

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
            print(UserT)
            print(type(UserT))
            print(self.User.id)
            print(type(self.User.balance))
            UserTT = (UserT, )
            self.cursor.execute(self.sqlCT, UserTT)

            balanceT = self.cursor.fetchone()

            if balanceT != None and int(UserT) != self.User.id:
                balanceT = balanceT[0]

                balance = int(self.User.balance) - int(Hm)

                balanceT = balanceT + int(Hm)
                
                if balance > 0:
                    self.User.balance = balance
                    FChange = (balance, self.User.id)
                    TChange = (balanceT, UserTT[0])
                    self.cursor.execute(self.sqlC, FChange)
                    self.con.commit()
                    self.cursor.execute(self.sqlC, TChange)
                    self.con.commit()
                    self.TransferHistoryChange(self.User.id, UserT, Hm)
                else:
                    print("Not enough money")
            else:
                print("Wrong id")

    def TransferHistoryChange(self, UserF, UserT, Hm):
        today = datetime.datetime.now()
        fullDay =  today.strftime("%x") + " " + today.strftime("%X")
        historyChange = (str(UserF), UserT, fullDay, Hm)
        self.cursor.execute(self.sqlAH, historyChange)
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
                

