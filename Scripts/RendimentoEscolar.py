import numpy as np
import matplotlib.pyplot as plt 

semestres = ['1° Invest', '2° Invest', '3° Invest/DOC', '4° Invest/INPL', '5° Finalizaçao', '6° Finalizaçao/DEV ']
investimentos = [4, 4, 6, 5, 5, 6]
aprovadas = [2, 3, 3, 5, 6, 6]
startup = [2, 1, 3, 0, 7, 4]

totais_investimentos = [4, 8, 14, 19, 24, 30]
totais_aprovada = [2, 4, 7, 12, 18, 24]

plt.style.use('classic')

plt.plot(semestres, investimentos, color = "white", linewidth = 2.5) #coloramento e tamanho da linha
plt.plot(semestres, totais_aprovada, color = "green", linewidth = 2.5)
plt.plot(semestres, startup, color = "red", linewidth = 2.5)
plt.plot(semestres, totais_investimentos, color = "purple", linewidth = 2.5)

plt.show()