num1 = float(input("Intruduza um numero: "))
num2 = float(input("Intruduza outro numero: "))
operacao = input("Escolha a operacao que queira (+,-,*,/): ")

if operacao == "+":
    soma = num1 + num2
    print("A soma e: ",soma)
elif operacao == "-":
    sub = num1 - num2
    print("A subtracao e: ",sub)
elif operacao == "*":
    mult = num1 * num2
    print("A multiplicao e: ",mult)
elif operacao == "/":
    div = num1 / num2
    print("A divisao e: ",div)
else:
    print("Nao intrudoziu uma operacao")
