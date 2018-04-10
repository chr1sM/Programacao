num = int(input("Introduza um numero inteiro: "))

print("Os 5 numeros antes do", num, "são: ")
for i in range(num - 1, num - 6, -1):
    print(i, end=" ")

print()

print("Os 5 numeros depois de", num, " são: ")
for i in range(num + 1, num + 6, 1):
    print(i, end=" ")
