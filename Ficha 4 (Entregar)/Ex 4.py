def numero(n):
    if n > 0:
        numero(n -1)
    print(n)
num = int(input('Introduza um numero: '))

numero(num)