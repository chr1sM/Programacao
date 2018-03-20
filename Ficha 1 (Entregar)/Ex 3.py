peso = float(input("Introduza o seu peso: "))
altura = float(input("Introduza a sua altura em metros: "))

imc = peso / altura ** 2

print("O seu indic de massa corporal e {0:.2f}".format(imc))