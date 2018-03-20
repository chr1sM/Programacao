num1 = int(input("Intruduza um numero: "))
num2 = int(input("Intruduza outro numero: "))
num3 = int(input("Intruduza o ultimo numero: "))

if num1 > num2 and num2 > num3:
    print("Maior:",num1,"Medio:",num2,"Menor:",num3)

elif num2 > num3 and num3 > num1:
    print("Maior:",num1,"Medio:",num3,"Menor:",num2)

elif num2 > num1 and num1 > num3:
    print("Maior:",num2,"Medio:",num1,"Menor:",num3)

elif num2 > num3 and num3 > num1:
    print("Maior:",num2,"Medio:",num3,"Menor:",num1)

elif num3 > num2 and num2 > num1:
    print("Maior:",num3,"Medio:",num2,"Menor:",num1)

elif num3 > num1 and num1 > num2:
    print("Maior:",num3,"Medio:",num1,"Menor:",num2)