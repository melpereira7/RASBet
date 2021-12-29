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
                if self.rb.verifica_credenciais(mail,pw):
                    print("yes")
                else:
                    print("no")
            op = int(self.menu())

