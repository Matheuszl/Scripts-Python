listaInt = [1,2,4,7,8,2]
listaStr = ['a','b','c']
print("Lista de Int: ", listaInt)
print("Lista de Str: ", listaStr)
#print(lista[0])

#adciona no final da lista
listaInt = listaInt + [7]
print("Lista de Int: ", listaInt)

#adciona no inicio da lista
listaInt = [0] + listaInt
print("Lista de Int: ", listaInt)

#concatena duas lista no final
lista2 = [8,8,8,8]
lista2 = lista2 + listaInt
print(lista2)

#Usando funçoes
#funçao append add na ultima posiçao da lista
lista3 = [0,1,2]
lista3.append(3)
print(lista3)

#funçao del para excluir um dado da lista por posiçao
del(lista3[2])
print(lista3)