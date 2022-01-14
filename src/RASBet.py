import threading
import json
import requests
import pandas as pd

from ApostaDAO import ApostaDAO
from UserDAO import UserDAO
from ApostaUserDAO import ApostaUserDAO


class RASBet:
    URL = 'http://127.0.0.1:5000/info' #url da api, neste caso está no meu localhost -- CORRER SERVER.PY

    def __init__(self):
        self.autenticado = ""
        self.bets = ApostaDAO() # -- data object access
        self.users = UserDAO()
        
    ## -- buscar dados à api e guardar na bd -- ##
    def get_bets_all(self):
        # access BettingAPI - RESTApi - ver como aceder em python
        data = json.loads(requests.get(self.URL).text)
        normalized_dict = pd.json_normalize(data, record_path=['listEventsAll'])
        data = pd.DataFrame.from_dict(normalized_dict, orient='columns')
        self.bets.delete_all()
        for index in data.index:
            d = data.iloc[index]
            if d['event.sport'] == 'soccer' or d['event.sport'] == 'football':
                self.bets.addFootball(d['event.sport'],d['event.team1'],d['event.team2'],d['event.result_odd.home'],d['event.result_odd.tie'],d['event.result_odd.away'])
            elif d['event.sport'] == 'f1':
                self.bets.addF1(d['event.drivers'],d['event.odds'])
        t = threading.Timer(60,self.get_bets_all)
        t.daemon = True
        t.start()

    ## -- buscar apostas disponíveis -- ##
    def get_bets(self):
        return self.bets.get_all()
    
    ## -- adicionar novo user -- ##
    def adiciona_registo(self,mail,name,pw,credit): 
        self.users.add(mail,name,pw,credit)
    
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


