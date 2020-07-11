print("Python do 0 \n")

#input: nome da variavel = tipo da variavel(input("texto que interresa"))  | type(nome) testa o tipo
nome = str(input("Nome: "))
idade = int(input("Idade:"))

#apenas um modelo de output tem varios
print("Usuario \n Nome:", nome, "Idade:", idade)

#modelo simples de if/else | elifi quando presisa testar varias condiçoes

if idade > 0 and idade < 18:
    print(nome," voce é menor de idade!")
elif idade > 18:
    print(nome," voce é maior de idade!")
else:
    print("Valor invalido!")









