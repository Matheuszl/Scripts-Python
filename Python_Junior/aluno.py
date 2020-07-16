class Aluno:
    def __init__(self, nome, idade, matricula, auxilioRU = False):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula  
        self.auxilioRU = auxilioRU
    
    def AuxilioRU(self):
        self.auxilioRU = True
    
    def ExibirDados(self):
        print(self.nome, self.idade, self.matricula, self.auxilioRU)

print(" |Cadastrar aluno| ")
nome = str(input("Nome: "))
idade = int(input("Indade: "))
matricula = int(input("Matricula: "))
auxilioRU = input("Auxilio RU: ")
a1 = Aluno(nome, idade, matricula, auxilioRU)
a1.ExibirDados()
