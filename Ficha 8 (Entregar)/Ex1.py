import random
NUM_VALORES = 5
NUM_MAX = 30

file = open("teste.txt", "a")

for n in range(NUM_VALORES):
    a = str(random.randint(0,NUM_MAX)) + "\n"
    file.write(a)

file.close()