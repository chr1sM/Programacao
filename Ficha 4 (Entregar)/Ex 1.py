def login(username,password):
        user = "admin"
        passe = "admin123"

        if username == user and password == passe:
            return True
        return False

def validar():
    contar = 0
    while contar != 3:
        print('Insira o nomer de utilizador e password')
        username = input("Username: ")
        password = input("Password: ")
        if login(username,password):
            print("Login sucessful")
            break
        else:
            print('Username ou Password estao errados')
        contar += 1
        if contar >= 3:
            print('Exedeu ao numero de tentativas')

validar()