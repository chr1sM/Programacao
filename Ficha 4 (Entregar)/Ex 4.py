num = int(input('Introduza um numero: '))

def numero(n):
    if n > 0:
        numero(n -1)
    print(n)

numero(num)