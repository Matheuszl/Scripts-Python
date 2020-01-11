import numpy as np

print('Calculo do IMC')
# IMC é a sigla para Índice de Massa Corpórea, parâmetro adotado pela Organização Mundial de Saúde para calcular o peso ideal de cada pessoa.
# O índice é calculado da seguinte maneira: 
# divide-se o peso do paciente pela sua altura elevada ao quadrado.
#  Diz-se que o indivíduo tem peso normal quando o resultado do IMC está entre 18,5 e 24,9.
# #

altura = [1.60, 1.70, 1.75, 1.80]
peso = [50, 60, 70, 80]

nAltura = np.array(altura)
nPeso = np.array(peso)

imc = nPeso / nAltura ** 2

print(imc)