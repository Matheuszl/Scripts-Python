#O comando while faz com que um conjunto de instruções seja executado enquanto uma condição é atendida. 
#Quando o resultado dessa condição passa a ser falso, a execução do loop é interrompida,

print("Executando 1° while \n")
cont = 0
while cont < 5:
    cont += 1
    print(cont)
else:
    print("Fim do 1° While: ", cont,"\n")

print("Executando 2° While \n")
cont = 0
while cont < 10:
    cont += 1
    if cont == 6:
        print("aqui x=6")
        break
else:
    print("Fim do 2° While \n")

condiçao = 0
while condiçao != 10:
    condiçao = int(input("Chute um valor: (10)"))
else:
    print("Fim do 3° While!")

#Metodo nao muito formal
resposta = "S"
while resposta == "S":
    numero = int(input("Digite um valor: "))
    if numero == 10:
        print("Acertou!")
        break
    resposta = str(input("Tentar novamente? [S/N]")).upper()
else:
    print("Fim do 4° While \n")

while True:
    numero = int(input("Digite um numero: "))
    if numero == 10:
        print("Acertou!")
        break

    resposta = int(input("tentar novamente? [1-Sim/2-Nao]"))
    if resposta == 1:
        True
    elif resposta == 2:
        break    
else:
    print("Fim do 5° While \n")
