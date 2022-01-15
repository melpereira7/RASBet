import mysql.connector

class CreditosUserDAO:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="root", 
            database="rasdb")
        self.mycursor = self.mydb.cursor()

    def get_all(self,mail):
        credit = {}
        self.mycursor.execute(f"SELECT * FROM CreditosUser WHERE User_mail = {mail}")
        for (moeda,creditos,_) in self.mycursor.fetchall():
            credit.update({moeda:creditos})
        return credit

    def add_creditos(self,mail,credit,moeda):
        self.mycursor.execute(f"INSERT INTO CreditosUser (moeda, creditos, User_mail) VALUES {moeda,credit,mail} \
                                            ON DUPLICATE KEY UPDATE creditos = creditos + {credit}")
        self.mydb.commit()

    def get_creditos(self, mail, moeda):
        self.mycursor.execute(f"SELECT creditos FROM CreditosUser where User_mail = '{mail}' AND moeda = '{moeda}'")
        return self.mycursor.fetchone()

    def subtrai_creditos(self, mail, credit, moeda):
        self.mycursor.execute(f"UPDATE CreditosUser SET creditos = creditos - {credit} WHERE User_mail = '{mail}' AND moeda = '{moeda}'")
        self.mydb.commit()

    def get_all_creditos(self,mail):
        self.mycursor.execute(f"SELECT SUM(creditos) FROM CreditosUser WHERE User_mail = {mail}")
        return self.mycursor.fetchone()