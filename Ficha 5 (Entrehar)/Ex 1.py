from random import randint
import time
import re
def validaremail(email):

    if len(email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$)" , email) != None:
            return True
        return False
    if validaremail("my.email@gmail.com") == True :
        print("Este email e valido")
    else:
        print("Este email nao e vaildo")

class user():

    def __init__(self):
        self.nome = None
        self.email = None
        self.passe = None
        self.id = None
        self.resp_secreta = None
        self.bloquear = False
        self.data_criacao = None
    
    def login_user(self):
        contar = 0
        if self.bloquear == True:
            resposta = input("Pergunta de seguranca: ")
            while resposta != self.resp_secreta:
                resposta = input("Pergunta de seguranca: ")
            else:
                self.bloquear = False   
                utilizador1.login_user()
        while contar < 3:
            login_email = input("Email: ")
            login_password = input("Password: ")
            if self.email == login_email and self.passe == login_password:
                print("Logou com successo")
                break
            else:
                print("Login errado!")
                contar += 1
        else:
            print("Utilizador bloqueado")
            self.bloquear = True
            utilizador1.login_user()
                      
print("Introduzir dados para o user1")
utilizador1 = user()
utilizador1.nome = input("Nome do user: ")
utilizador1.email = input("Email do utilizador: ")
utilizador1.passe= input("Password do utilizador: ")
utilizador1.id = "{}-{}".format(randint(100, 999),randint(1000, 9999))
utilizador1.resp_secreta = input("Resposta secreta do utilizador: ")
utilizador1.data_criacao = time.strftime("%d/%m/%Y")

print("Introduzir dados para o user2")
utilizador2 = user()
utilizador2.nome = input("Nome do user: ")
utilizador2.email = input("Email do utilizador: ")
utilizador2.passe = input("Password do utilizador: ")
utilizador2.id = "{}-{}".format(randint(100, 999),randint(1000, 9999))
utilizador2.resp_secreta = input("Resposta secreta do utilizador: ")
utilizador2.data_criacao = time.strftime("%d/%m/%Y")

utilizador1.login_user()