num = int(input('Introduza um numero: '))

def numero(n):
    if n == -1:
        return 0
    elif numero(n - 1):
        return n
    print(n)

numero(num)