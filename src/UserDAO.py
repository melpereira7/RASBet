import mysql.connector

class UserDAO:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="root", 
            database="rasdb")
        self.mycursor = self.mydb.cursor()
    
    def add(self, mail, name, pw, credit):
        val = (mail,name,pw,credit)
        self.mycursor.execute(f"INSERT INTO User (mail, name, password, credits) VALUES {val}")
        self.mydb.commit()

    def get(self, mail):
        self.mycursor.execute(f"SELECT password FROM User WHERE mail = '{mail}'")
        return self.mycursor.fetchone()

    def get_name(self,mail):
        self.mycursor.execute(f"SELECT name FROM User WHERE mail = '{mail}'")
        return self.mycursor.fetchone()
    
    def contains(self,mail):
        self.mycursor.execute(f"SELECT * FROM User WHERE mail = '{mail}'")
        if self.mycursor.fetchone() == 'None':
            return False
        else:
            return True