import tkinter as tk
from tkinter import *
import webbrowser

win = tk.Tk() ## criaçao da tela
win.title("Tradutor") ## titulo da janela
win.geometry("550x450") ## tamanho da tel

## Sequancia de metodos que fazem a ligaçao com o site
def google():
    webbrowser.open("https://www.google.com.br")

def youtube():
    webbrowser.open("https://www.youtube.com")

def twitter():
    webbrowser.open("https://twitter.com/home?lang=pt-br")

def facebook():
    webbrowser.open("https://www.facebook.com")

def linkdin():
    webbrowser.open("https://www.linkedin.com/in/matheus-zalamena/")


igoogle = PhotoImage(file=r"C:\Users\matza\OneDrive\Documentos\TESTE\Scripts-Python\google.png")
google = tk.Button(win, image = igoogle, command = google)
google.grid(row=0, column=0)

iyoutube = PhotoImage(file=r"C:\Users\matza\OneDrive\Documentos\TESTE\Scripts-Python\youtube.png")
youtube = tk.Button(win, image = iyoutube, command = youtube)
youtube.grid(row=0, column=1)

itwitter = PhotoImage(file=r"C:\Users\matza\OneDrive\Documentos\TESTE\Scripts-Python\linkdin.png")
twitter = tk.Button(win, image = itwitter, command = twitter)
twitter.grid(row=1, column=0)

ifacebook = PhotoImage(file=r"C:\Users\matza\OneDrive\Documentos\TESTE\Scripts-Python\face.png")
facebook = tk.Button(win, image = ifacebook, command = facebook)
facebook.grid(row=1, column=1)




win.mainloop()