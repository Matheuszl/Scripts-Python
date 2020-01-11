from random import uniform
from random import randint

texto = []

def obterTexto():
    for i in range(1, 100):
        texto.append(str(uniform(1.50, 2.20)) +';'+ str(uniform(50, 120)) +';'+ str(randint(0,10)) + '\n')

def gerarArquivo():
    arq = r'C:\Users\matza\OneDrive\Documentos\TESTE\Scripts-Python\peso.csv.txt'
    entrada = open(arq, 'w+', encoding='UTF-8')
    obterTexto()
    entrada.writelines(texto)
    entrada.close()

if __name__ == "__main__":
    gerarArquivo()