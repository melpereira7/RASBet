import mysql.connector

from Bet import FootballBet, F1Bet

class ApostaDAO:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="qwerty1234", 
            database="rasdb")
        self.mycursor = self.mydb.cursor()

    def addFootball(self,sport,home_team,away_team,odd_home,odd_tie,odd_away):
        val = (sport,home_team,away_team,odd_home,odd_tie,odd_away)
        self.mycursor.execute(f"INSERT INTO Aposta (sport,home_team,away_team,odd_home,odd_tie,odd_away) VALUES {val}")
        self.mydb.commit()

    def addF1(self,drivers,odds):
        self.mycursor.execute(f"INSERT INTO Aposta (sport) VALUES ('f1')")
        id_driver_odd = self.mycursor.lastrowid
        for driver, odd in zip(drivers,odds):
            self.mycursor.execute(f"INSERT INTO DriverOdds (driver, odd, Aposta_id) VALUES {(driver,odd,id_driver_odd)}")

    def delete_all(self):
        self.mycursor.execute("SET SQL_SAFE_UPDATES = 0")
        self.mycursor.execute("DELETE FROM DriverOdds")
        self.mycursor.execute("DELETE FROM Aposta")
        self.mycursor.execute("SET SQL_SAFE_UPDATES = 1")

    def get_all(self):
        bets = []
        drivers = []
        odds = []
        self.mycursor.execute("SELECT * FROM Aposta")
        for (id_aposta,sport,home_team,away_team,home_odd,tie_odd,away_odd) in self.mycursor.fetchall():
            if sport == 'soccer' or sport == 'football':
                bet = FootballBet(id_aposta,sport,home_team,away_team,home_odd,tie_odd,away_odd)
            elif sport == 'f1':
                self.mycursor.execute(f"SELECT * FROM DriverOdds WHERE Aposta_id = {id_aposta}")
                for (_,driver,odd,_) in self.mycursor.fetchall():
                    drivers.append(driver)
                    odds.append(odd)
                bet = F1Bet(id_aposta,sport,drivers,odds)
            bets.append(bet)
        return bets