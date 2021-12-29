import textwrap
import mysql.connector

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
                name = input("Enter your name: ")
                pw = input("Enter a password: ")
                pw2 = input("Confirm your password: ")
                if pw == pw2:
                    credit = int(input("Enter an amount to deposit: "))
                    self.rb.adiciona_registo(mail,name,pw,credit)
                    print("You are now registered!")
                else:
                    print("The passwords do not match!")
            elif op == 3:
                mail = input("Enter your email: ")
                pw = input("Enter your password: ")
                valido = self.rb.verifica_credenciais(mail,pw)
                if valido == 'True':
                    self.runUser(self.rb.get_name(mail))
                elif valido == 'False':
                    print("Wrong password, please try again")
                elif valido == 'User':
                    print("User does not exist!")
            op = int(self.menu())

    def menuUser(self,name):
        return input(textwrap.dedent(f'''
                Bem-vind@, {name}!
                1 - Listar apostas disponíveis
                2 - Realizar aposta
                3 - Adicionar créditos
                4 - Levantar créditos
                5 - Listar apostas realizadas
                0 - Terminar sessão
                '''))
        
    def runUser(self,name):
        op = int(self.menuUser(name))
        while op != 0:
            if op == 1:
                for bet in self.rb.get_bets():
                    print(str(object=bet))
            elif op == 2:
                pass
            elif op == 3:
                pass
            elif op == 4:
                pass
            elif op == 5:
                pass
            op = int(self.menuUser(name))
        #termina sessão
