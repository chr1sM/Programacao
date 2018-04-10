print("Introduza o seu voto de 1-4 , sendo 0 um voto nulo , 9 um voto branco e -1 para terminar : ")
voto = int(input("Qual e a sua opcao? "))
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
votonulo = 0
votobranco = 0

while voto != -1:
    if voto == 1:
        candidato1 += 1
    if voto == 2:
        candidato2 += 1
    if voto == 3:
        candidato3 += 1
    if voto == 4:
        candidato4 += 1
    if voto == 9:
        votonulo += 1
    if voto == 0:
        votobranco += 1
    print("Introduza o seu voto de 1-4 , sendo 0 um voto nulo , 9 um voto branco e -1 para terminar : ")
    voto = int(input("Qual e a sua opcao? "))

total = candidato1 + candidato2 + candidato3 + candidato4 + votobranco + votonulo
percentagem_cand1 = (candidato1 * 100) / total
percentagem_cand2 = (candidato2 * 100) / total
percentagem_cand3 = (candidato3 * 100) / total
percentagem_cand4 = (candidato4 * 100) / total
percentagem_vbranco = (votobranco * 100) / total
percentagem_vnulo = (votonulo * 100) / total

print("O voto total destas elecoes foram: ", total)
print("O candidato 1 teve", candidato1, "votos e teve um percentagem de", percentagem_cand1, "%")
print("O candidato 2 teve", candidato2, "votos e teve um percentagem de", percentagem_cand2, "%")
print("O candidato 3 teve", candidato3, "votos e teve um percentagem de", percentagem_cand3, "%")
print("O candidato 4 teve", candidato4, "votos e teve um percentagem de", percentagem_cand4, "%")
print("O total de votos brancos foi de", votobranco, "votos e teve um percentagem de", percentagem_vbranco, "%")
print("O total de votos nulos foi de", votonulo, "votos e teve um percentagem de", percentagem_vnulo, "%")


