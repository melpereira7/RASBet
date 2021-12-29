class FootballBet:

    def __init__(self,id,sport,home_team,away_team,odd_home,odd_tie,odd_away):
        self.id = id
        self.sport = sport
        self.home_team = home_team
        self.away_team = away_team
        self.odd_home = odd_home
        self.odd_tie = odd_tie
        self.odd_away = odd_away

    def __str__(self) -> str:
        return "{id: " + str(self.id) + " sport: " + self.sport + " | home_team: " + self.home_team +\
            " | away_team: " + self.away_team + " | odd_home: " + str(self.odd_home) + " | odd_tie: " +\
            str(self.odd_tie) + " | odd_away: " + str(self.odd_away) + "}"

class F1Bet:

    def __init__(self,id,sport,drivers,odds):
        self.id = id
        self.sport = sport
        self.drivers = drivers
        self.odds = odds

    def __str__(self) -> str:
        return "{id: " + str(self.id) + " sport: " + self.sport + " | drivers: [" + ",".join(self.drivers) +\
            "] | odds: [" + ",".join([str(element) for element in self.odds]) + "]}"