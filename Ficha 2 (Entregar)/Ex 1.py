nota1 = float(input("Introduza a primeira nota (0-20):"))
while nota1 < 0.0 or nota1 > 20.0:
    print("Erro: Nao introdoziu os valores corretos")
    nota1 = float(input("Introduza a primeira nota (0-20):"))

nota2 = float(input("Introduza a segunda nota (0-20):"))
while nota2 < 0.0 or nota2 > 20.0:
    print("Erro: Nao introdoziu os valores corretos")
    nota2 = float(input("Introduza a segunda nota (0-20):"))

nota3 = float(input("Introduza a terceira nota (0-20):"))
while nota3 < 0.0 or nota3 > 20.0:
    print("Erro: Nao introdoziu os valores corretos")
    nota3 = float(input("Introduza a terceira nota (0-20):"))

media = float((nota1 * 25 + nota2 * 35 + nota3 * 40) / 100)

if media >= 9.5:
    print("O aluno esta aprovado com", media, "de media")
else:
    print("O aluno esta reprovado com", media, "de media")

media = float((nota1 * 25 + nota2 * 35 + nota3 * 40) / 100)

if media >= 9.5:
    print("O aluno esta aprovado com",media,"de media")
else:
    print("O aluno esta reprovado com",media,"de media")
