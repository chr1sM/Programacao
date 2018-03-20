nota1 = float(input("Introduza o valor da primeira nota (0-20): "))
nota2 = float(input("Introduza o valor da segunda nota (0-20): "))
nota3 = float(input("Introduza o valor da terceira nota (0-20): "))

media = float((nota1 * 25 + nota2 * 35 + nota3 * 40) / 100)
media_int = float((nota1 * 25 + nota2 * 35 + nota3 * 40) // 100)
media_mod = (nota1 * 25 + nota2 * 35 + nota3 * 40) % 100

print("A media das notas e", media ,"%")
print("A media inteira e:", media_int)
print("O modulo da divisao e:", int(media_mod))

