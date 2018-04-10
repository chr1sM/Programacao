linha = int(input('Quantas linhas deseja? '))
caracter = input('Escolha o caracter do desenho: ')
coluna = int(input('Quantas colunas deseja? '))

def retangulo(linha, caracter, coluna):
     
    for a in range(1, linha + 1):
        for b in range(1, coluna + 1):
            if a == 1 or a == linha or b == 1 or b == coluna:
                print(caracter, end="")            
            else:
                print(" ", end="")            
        print()

retangulo(linha, coluna, caracter)