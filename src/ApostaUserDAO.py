import mysql.connector

from ApostaUser import ApostaUser

class ApostaUserDAO:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="qwerty1234", 
            database="rasdb")
        self.mycursor = self.mydb.cursor()

    def add(self,result,amount,aposta_id,user_mail):
        val = (result,amount,aposta_id,user_mail)
        self.mycursor.execute(f"INSERT INTO ApostaUser (result,amount,Aposta_id,User_mail) VALUES {val}")
        self.mycursor.commit()
    
    def get_all(self):
        betsUser = []
        self.mycursor.execute(f"SELECT * FROM ApostaUser")
        for (id,result,amount,aposta_id,user_mail) in self.mycursor.fetchall():
            betUser = ApostaUser(id,result,amount,aposta_id,user_mail)
            betsUser.append(betUser)
        return betsUser
