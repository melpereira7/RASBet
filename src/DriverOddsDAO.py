import mysql.connector

class DriverOddsDAO:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="root", 
            database="rasdb")
        self.mycursor = self.mydb.cursor()

    def get_all(self,id_aposta):
        driverOdds = {}
        self.mycursor.execute(f"SELECT * FROM DriverOdds WHERE Aposta_id = {id_aposta}")
        for (_,driver,odd,_) in self.mycursor.fetchall():
            driverOdds.update({driver:odd})
        return driverOdds