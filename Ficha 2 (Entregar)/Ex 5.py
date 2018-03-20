saldo = int(input("Intruduza o saldo da sua conta bancaria: "))
print("Escolha a opcao que deseja:")
print("1)Creditar")
print("2)Debitar")
opcao = input("Intoduza a opcao: ")

if opcao == "1":
    credito = float(input("Qual e o valor que quer creditar na sua conta?"))
    res = saldo + credito
    print("Voce ficou com",res,"€ na sua conta")
elif opcao == "2":
    debito = float(input("Quando deja debitar da sua conta?"))
    res = saldo - debito
    if res < 0:
       print("Nao tem saldo suficiente na conta")
    else:
        print("Voce ficou com",res,"€ na sua conta")