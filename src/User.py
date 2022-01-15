from ApostaUserDAO import ApostaUserDAO
from CreditosUserDAO import CreditosUserDAO

class User:
    def __init__(self,mail,name,pw):
        self.mail = mail
        self.name = name
        self.pw = pw
        self.credit = CreditosUserDAO()
        self.bets = ApostaUserDAO()
    
    def get_all(self):
        self.credit.get_all(self.mail)

    def add_creditos(self,credit,moeda):
        self.credit.credit.add_creditos(self.mail,credit,moeda)

    def get_creditos(self, moeda):
        self.credit.get_creditos(self.mail, moeda)

    def subtrai_creditos(self, credit, moeda):
        self.credit.subtrai_creditos(self.mail, credit, moeda)

    def get_soma_creditos(self):
        self.credit.get_all_creditos(self.mail)
    