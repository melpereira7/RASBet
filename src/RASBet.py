import threading
import json
import requests
import pandas as pd

from ApostaDAO import ApostaDAO
from UserDAO import UserDAO


class RASBet:
    URL = 'http://127.0.0.1:5000/info' #url da api, neste caso está no meu localhost -- CORRER SERVER.PY

    def __init__(self):
        self.autenticado = ""
        self.bets = ApostaDAO() # -- data object access
        self.users = UserDAO()

    ## -- buscar dados à api e guardar na bd -- ##
    def get_bets_all(self):
        # access BettingAPI - RESTApi
        data = json.loads(requests.get(self.URL).text)
        normalized_dict = pd.json_normalize(data, record_path=['listEventsAll'])
        data = pd.DataFrame.from_dict(normalized_dict, orient='columns')
        self.bets.delete_all()
        for index in data.index:
            d = data.iloc[index]
            if d['event.sport'] == 'soccer' or d['event.sport'] == 'football':
                self.bets.addFootball(d['event.id'],d['event.sport'],d['event.team1'],d['event.team2'],d['event.result_odd.home'],d['event.result_odd.tie'],d['event.result_odd.away'])
            elif d['event.sport'] == 'f1':
                self.bets.addF1(d['event.id'],d['event.drivers'],d['event.odds'])
        t = threading.Timer(60,self.get_bets_all)
        t.daemon = True
        t.start()

    ## -- mail do user autenticado -- ##
    def set_autenticado(self,mail):
        self.autenticado = mail

    ## -- buscar apostas disponíveis -- ##
    def get_bets(self):
        return self.bets.get_all()

    def get_bet(self,idAposta):
        return self.bets.get_bet(idAposta)
    
    ## -- adicionar novo user -- ##
    def adiciona_registo(self,mail,name,pw,moeda,credit): 
        self.users.add(mail,name,pw)
        self.users.get_user(mail).add_creditos(moeda,credit)
    
    ## -- get do nome de determinado user -- ##
    def verifica_credenciais(self,mail,pw):
        if self.users.contains(mail):
            if pw == self.users.get_password(mail=mail)[0]:
                return 'True'
            else:
                return 'False'
        else:
            return 'User'

    ## -- get do nome de determinado user -- ##
    def get_name(self,mail):
        return self.users.get_name(mail)[0]
    
    ## -- check se já existe um user com determinado mail na bd -- ##
    def contains_user(self,mail):
        return self.users.contains(mail);

    def executa_transferencia(self, n, iban):
        # send the money to the iban account
        print(f"You will get the {n} in your account in 5 week days.")
            
    def levantar_creditos(self, n, iban, moeda):
        user = self.users.get_user(self.autenticado)
        (creditos,) = user.get_creditos(moeda)
        if creditos - n < 0:
            return False
        else:
            user.subtrai_creditos(n, moeda)
            self.executa_transferencia(n, iban)
            return True

    def add_credits(self,creditos,moeda):
        user = self.users.get_user(self.autenticado)
        user.add_creditos(creditos,moeda)

    def get_bets_user(self):
        user = self.users.get_user(self.autenticado)
        return user.bets.get_all()
        
