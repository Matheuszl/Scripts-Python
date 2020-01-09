import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

# A busca funciona na linguagem inglesa e o resultado tambem
# Busque por palavras ou frases


win = Tk() ## criaçao da tela
win.title("Buscar") ## titulo da janela
win.geometry("400x100") ## tamanho da tela

def pesquisar():
    pesquisa = entry.get()
    pergunta = wikipedia.summary(pesquisa)
    showinfo("Resultado: ",pergunta)

janela = Label(win, text="Busca: ")
janela.grid(row=0, column=0)

entry =Entry(win)
entry.grid(row=0, column=1) #mudar

botao = Button(win, text="Pesquisar", command = pesquisar)
botao.grid(row=2, column=1)

win.mainloop()