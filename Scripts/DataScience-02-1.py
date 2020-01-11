import numpy as np

def tabela(valorImc):
    if valorImc < 16:
        return str(valorImc) + ': Magreza severa'
    elif valorImc < 18:
        return str(valorImc) + ': Magreza moderada'
    elif valorImc < 25:
        return str(valorImc) + ': Saudavel'
    elif valorImc < 35:
        return str(valorImc) + ': Sobrepeso'
    elif valorImc < 45:
        return str(valorImc) + ': Obesidade'

altura, peso, forca = np.loadtxt(r'C:\Users\matza\OneDrive\Documentos\TESTE\Scripts-Python\peso.csv.txt',
                                delimiter=';',
                                unpack=True,
                                dtype='float')

imc = peso / altura ** 2

#qual o menor valor dessa populaçao?
print('Min: '+ tabela(np.amin(imc)))
#qual o maior valor dessa populaçao?
#print("Max: "+ tabela(np.amax(imc))) ta com erro