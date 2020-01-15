import numpy as np
import matplotlib.pyplot as plt 



semestres = ['primeiro', 'segundo', 'terceiro', 'quarto']
cadeiras = [4, 4, 6, 5]
aprovadas = [2, 3, 3, 5]
reprovadas = [2, 1, 3, 0]

totais_cadeiras = [4, 8, 14, 19]
totais_aprovada = [2, 4, 7, 12]
1

plt.style.use('dark_background')


plt.plot(semestres, cadeiras, color = "white", linewidth = 2.5) #coloramento e tamanho da linha
plt.plot(semestres, totais_aprovada, color = "green", linewidth = 2.5)
plt.plot(semestres, reprovadas, color = "red", linewidth = 2.5)
plt.plot(semestres, totais_cadeiras, color = "purple", linewidth = 2.5)

plt.show()
