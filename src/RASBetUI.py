import textwrap

from RASBet import RASBet

class RASBetUI:

    def __init__(self) -> None:
        self.rb = RASBet()
        self.rb.get_bets_all()

    def menu(self):
        return input(textwrap.dedent('''
                Bem-vindo ao RASBet!
                1 - Listar apostas
                2 - Registar
                3 - Autenticar
                0 - Sair
                '''))

    def run(self):
        op = int(self.menu())
        while op != 0:
            if op == 1:
                for bet in self.rb.get_bets():
                    print(str(object=bet))
            elif op == 2:
                mail = input("Enter your email: ")
                if self.rb.contains_user(mail):
                    print("Email já registado!")
                else:
                    name = input("Enter your name: ")
                    pw = input("Enter a password: ")
                    pw2 = input("Confirm your password: ")
                    if pw == pw2:
                        credit = float(input("Enter an amount to deposit: "))
                        moeda = self.selectCode()
                        self.rb.adiciona_registo(mail,name,pw,moeda,credit)
                        print("You are now registered!")
                    else:
                        print("The passwords do not match!")
            elif op == 3:
                mail = input("Enter your email: ")
                pw = input("Enter your password: ")
                valido = self.rb.verifica_credenciais(mail,pw)
                if valido == 'True':
                    self.rb.set_autenticado(mail)
                    self.runUser(self.rb.get_name(mail))
                elif valido == 'False':
                    print("Wrong password, please try again")
                elif valido == 'User':
                    print("User does not exist!")
            op = int(self.menu())

    def menuUser(self,name):
        return input(textwrap.dedent(f'''
                Bem-vind@, {name}!
                1 - Realizar aposta
                2 - Adicionar créditos
                3 - Levantar créditos
                4 - Listar apostas realizadas
                0 - Terminar sessão
                '''))

    def selectCode(self):
        moeda = ''
        while not (moeda == 'EUR' or moeda == 'USD' or moeda == 'GBP' or moeda== 'ADA'):
            print("---------- MOEDAS -----------")
            print("EUR - Euro (€)")
            print("USD - United States dollar ($)")
            print("GBP - Pound Sterling (£)")
            print("ADA - Cardano ")
            moeda = input("Seleciona o código da moeda pretendia: ")
        return moeda
        
    def runUser(self,name):
        
        op = int(self.menuUser(name))
        while op != 0:
            if op == 1:
                # realizar uma aposta - checkar dados e adcionar na bd
                for bet in self.rb.get_bets():
                    print(str(object=bet))
                          
                print("Escolha o id da sua aposta:")
                id_aposta = int(input())
                bet =  self.rb.get_bet(id_aposta)
                if bet.sport == 'soccer' or bet.sport == 'football':
                    print("    1      X      2")
                    print("  " + str(bet.odd_home) + "  " + 
                          str(bet.odd_tie) + "  "  + str(bet.odd_away))
                    print("Qual a sua aposta 1 X 2 ?")
                    tipo = str(input())
                    if tipo =='1':
                        percentagem = bet.odd_home
                    elif tipo=='X':
                        percentagem = bet.odd_tie
                    elif tipo=='2':
                        percentagem = bet.odd_away
                    else:
                        break
                   



                elif bet.sport == 'f1':
                    
                    print("***ID CONDUTOR***. ***Nome condutor***.***ODDS***.")
                    n = 1
                    for  elem,odd in zip(bet.get_driver_odds()): 
                        print("("+ n + ") |                " + elem+"       |                "+str(odd))
                    print("Qual o competidor que deseja apostar?") 
                    competidor = str(input())
                    percentagem = bet.odds[n-1]
                    

           
                user = self.rb.users.get_user(self.rb.autenticado)
                print("As suas carteiras. A partir de qual deseja apostar?")
                dic = user.get_all()
                for key, value in dic.items():
                    print(key, value)
                    wallet = str(input())
           
            elif op == 2:
                creditos = float(input("Enter the number of credits: "))
                moeda = self.selectCode()
                self.rb.add_credits(creditos,moeda)
            elif op == 3:
                valido = False
                count = 0
                n = float(input("Enter the number of credits: "))
                iban = input("Enter your IBAN: ")
                moeda = self.selectCode()
                while not valido and count < 3:
                    valido = self.rb.levantar_creditos(n, iban, moeda)
                    if not valido:
                        print("Não existem tantos créditos na sua conta, tente novamente ")
                if count == 3:
                    print("You exceed the number of try")
            elif op == 4:
                lista = self.rb.get_bets_user()
                for elem in lista:
                    print(elem)
            else:
                print("Escolha uma oção das disponíveis.")
            ################ ADD FUNCIONALIDADES NOVAS ###############
            op = int(self.menuUser(name))
        if op == 0:
            self.rb.set_autenticado('') # terminar sessão
