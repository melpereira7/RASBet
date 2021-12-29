from ApostaUserDAO import ApostaUserDAO

class User:
    def __init__(self,mail,name,pw,credit):
        self.mail = mail
        self.name = name
        self.pw = pw
        self.credit = credit
        self.bets = ApostaUserDAO()
    