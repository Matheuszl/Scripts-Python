from tkinter import *
import pyqrcode

tela = Tk()# Criaçao da tela
tela.title("Gerador QR Code")# Titulo
tela.geometry("250x100")# Tamanho da tela

# -Metodo gerador
def met_gerador():
    url = jDados.get()
    qr = pyqrcode.create(url)
    save = qr.svg("QRcode.svg", scale=5)

# -Icones da tela
lTexto = Label(tela, text="Entrar com a URL: ", width=30)
lTexto.grid(row=0, column=0)

jDados = Entry(tela)
jDados.grid(row=1, column=0)

bEntrar = Button(tela, text="Gerar!", command = met_gerador)
bEntrar.grid(row=3, column=0)


tela.mainloop()