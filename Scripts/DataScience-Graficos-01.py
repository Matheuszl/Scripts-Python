import numpy as np
import matplotlib.pyplot as plt 
# Importaçao das bibliotecas numpy e matplotlit (pip install)

dados = np.linspace(2*np.pi, -2*np.pi, 100)
"""
1. A função linspace cria uma sequencia de números uniformemente espaçados entre os limites dados
2. A biblioteca matplotlib permite a criação de gráficos em 2D 
"""

y1 = np.sin(dados)
y2 = np.cos(dados)
y3 = np.sin(dados)+3*np.cos(dados)

plt.style.use('dark_background')
plt.figure(figsize=(10,6), dpi=80)
plt.plot(dados, y1, color = "red", linewidth = 2.5) #coloramento e tamanho da linha
plt.plot(dados, y2, color = "blue", linewidth = 2.5)
plt.plot(dados, y3, color = "white", linewidth = 2.5)
plt.ylim(-4,5)
plt.legend(('Função seno', 'Função coseno', 'Função seno(dados) + 3coseno(dados)'), 
prop = {'size': 10}, loc = 'upper right')

plt.title("Funçoes", color = 'white', fontsize = 18)

plt.show()