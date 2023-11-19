"""
	As listas em python não possuem um tamanho defionido, póde se adicionar elementos até que a memória
estoure, outro detalhe importante é que em uma lista pode ser trabalhado qualquer tipo de elemento, p
pode se adicionar desde inteiros a strings e até outras listas a uma lista

"""

#o dir mostra todos os metodos que podem ser aplicado ao tipo de dadop

print(type([]))

#pode se criar listas de diversas formas
###Para criar uma lista vazia:
lista = []

###Para criar uma lista de caracteres:
lista2 = ['e', 'd', 's', 'o', 'n']

###Para criar uma lista de numeros:
lista3 = [1, 2, 3, 4, 5]

###Ou podemos usar o metodo list que transforma qualquer variavel em uma lista

lista4 = list(range(10))

###como o metodo list podemos facilmente transfoprmar uma string em uma lista
nome = 'edson'
lista5 = list(nome)

###outro detalhe é que se pode buscar os elementos em uma lista facilmente, usando apenas o if:
numero = 3
if numero in lista4:
		print(f'encontrei o elemento {numero} na lista')
else:
		print(f'o elemento{numero} não foi encontrado na lista')



###podemos facilmente ordenar uma lista com o metodo sort

lista6 = [2, 4, 3, 5, 1, 9, 6, 7, 1]
lista6.sort()
print(lista6)

###com o metodo count, podemos facilmente contar quantas vezes o elemento ocorre em uma lista
print(lista6.count(numero))

###estes métodos podem ser usados tanto para string quanto caracteres, inteiros e outros

###para adicionar elementos a uma lista usamos o append, da seguinte forma
lista6.append(8)
print(lista6)

#neste caso pode-se adicionar apenas um elemento por vez em uma lista no python, porem pode se adicionar
#qualquer tipo de dado a lista, por exemplo outra lista

#lista6.append(lista2)
#print(lista6)

#para Adicionar mais de um elemento a lista individualmente usa se o extend
lista6.extend([1,2,3])
print(lista6)

###pode se também adicionar um elemento informando o idice que ele estara em sua lista, da seguinte forma
#lista6.insert(1, 'novo elemento')
#print(lista6)

### é possivel juntar duas listas da seguinte forma
###criando uma nova lista:
lista7 = lista6+lista3
print(lista7)
### ou também extendendo uma lista
lista6.extend(lista3)
print(lista6)

###para inverter uma lista temos duas maneiras, a priemira usando o reverse
lista6.reverse()
print(lista6)

###podemos também usar um operador para inverter apenas na hora de imprimir
print(lista6[::-1])
print(lista6)

###podemos copiar uma lista usa-se o metodo copy, da seguinte forma
lista7=lista2.copy()
print(lista7)

###para saber o tamanho de uma lista basta o metodo len
print(len(lista7))

#para remover o ultimo elemento de uma lista usa-se o pop,caso queira remover um elemento em especifico basta
#passar seu indice por parametro, *o pop também retorna o elemento que esta sendo removido
#para limpar basta usar o metodo clear

print(lista7)
#lista7.pop(2)
#lista7.clear()
print(lista7)

#é possivel usar o metodo split para converter uma string em uma lista:
string = 'edson auguisto'
print(string)
string = string.split()
print(string)
#por padrão o metodo separa pelo caractere de espaço, porem basta passar como parametro o separador que quer
#por exemplo o ','
#caso queira transformar uma lista em uma string basta usar:?
string = ' '.join(lista2)
print(string)

###para inverter uma lista basta usar o metodo reverse













