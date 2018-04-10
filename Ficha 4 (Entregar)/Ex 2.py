#1 euro = 1.2323 dolar
dolar = 1.2323
#1 dolar = 0.81148 euro
euro = 0.81148

print('Conversao de Euro(€) para Dolar($) ou Dolar($) para Euro(€)')
print('Introduza o valor e o caracter. ')
valor = float(input('Introduza o valor: '))
caracter = input('Escolha o caracter que queira E ou D: ')

def conversao(valor, caracter , dolar , euro):
    if caracter == "d":
        totald = valor * euro
        print('Conversao de dolares para euros {0:.2f} €'.format(totald))
    elif caracter == "e":
        totale = valor * dolar
        print('Conversao de euros para Dolares {0:.2f} $'.format(totale))

conversao(valor, caracter , dolar , euro)

