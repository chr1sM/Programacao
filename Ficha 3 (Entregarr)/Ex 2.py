num = int(input("Insira um numero "))
if num == 2:
    print("O numero", num, "e primo")
else:
    while num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("O numero", num, "nao e primo")
                break
            else:
                print("O numero", num, "e primo")
                break
        break
if num <= 1:
    print("Para ser primo tem de ser superior a 1, por isso o numero", num, "nao e possivel")