nome = 'edson'
lista = [1, 2, 3, 4, 5, 6]
numeros = range(1,10)



#iterando sobre uma string
for letra in nome:
		print(letra)

#iterando sobre uma lista
for numero in lista:
		print(numero)

#iterando sobre um range
#o valor final não é incluso

for numero in range(0,10):
		print(numero)



#enumerate, este retorna o indice e a letra da string

for indice, letra in enumerate(nome):
		print(indice)
		print(letra)

#ou pode se usar o indice para acessar o valor na posição
for indice, lewtra in enumerate(nome):
		print(nome[indice])

#e caso queira ignorar um dos valores retornados, basta uasr o _
for _, letra in enumerate(nome):
		print(letra)


#para imprimir sem o \n o print tem que ser feito de maneira diferente
for letra in nome:
		print(letra, end='')
