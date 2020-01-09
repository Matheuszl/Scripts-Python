import tkinter as tk
from googletrans import Translator

win = tk.Tk() ## criaçao da tela
win.title("Tradutor") ## titulo da janela
win.geometry("400x100") ## tamanho da tela

def tadutor():
    palavra = entry.get()
    translator = Translator(service_urls=['translate.google.com']) ## conecçao com o site tradutor 
    translation1 = translator.translate(palavra, dest="pt") ## escohe a linguagem pra qual sera traduzida
    label1 = tk.Label(win, text=f"Traduçao: {translation1.text}", bg="red")
    label1.grid(row=2, column=0)

janela = tk.Label(win, text="Palavra ou texto: ")
janela.grid(row=0, column=0, sticky="W")

entry = tk.Entry(win)
entry.grid(row=1, column=0)

botao = tk.Button(win, text="Traduzir", command = tadutor)
botao.grid(row=1, column=2)

win.mainloop()