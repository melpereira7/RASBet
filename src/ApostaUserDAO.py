import mysql.connector

class ApostaUserDAO:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="qwerty1234", 
            database="rasdb")
        self.mycursor = self.mydb.cursor()