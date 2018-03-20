nota1 = float(input("Introduza o valor da primeira nota (0-20): "))
nota2 = float(input("Introduza o valor da segunda nota (0-20): "))
nota3 = float(input("Introduza o valor da terceira nota (0-20): "))

media = float((nota1 * 25 + nota2 * 35 + nota3 * 40) / 100)

if media >= 9.5:
    print("O aluno esta aprovado com",media,"de media")
else:
    print("O aluno esta reprovado com",media,"de media")