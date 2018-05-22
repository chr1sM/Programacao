class aluno():

    def __init__(self,nome,numero):
        self.numero = numero
        self.nome = nome.title()
    def igual(self, aluno):
        return self.numero == aluno.numero

    def __str__(self):
        return "Numero {} | Nome {}".format(self.numero , self.nome)

#######################################

class turma():

    def __init__(self,nome,ano,listaAlunos):
       self.nome = nome
       self.ano = ""
       self.listaAlunos = []
       self.totalAlunos = 0

    def verificar(self,aluno):
       for i in range(self.totalAlunos):
           if self.listaAlunos[i].igual(aluno):
            return True
       return False

    def inserirAluno(self,aluno):
        if self.verificar(aluno) == False
           self.listaAlunos.append(aluno)
           self.totalAlunos += 1
           return True
        return False

    def inserAluno(self, numero, nome):
        aluno = aluno(numero, nome)
        return self.inserirAluno(self, aluno)