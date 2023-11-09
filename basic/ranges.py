#para o range temos um padrao para apenas um numero
#este vai de 0 a n-1
for numero in range(10):
		print(numero)

#é possivel também usaar um numero inicial, então vai do numero inicial até o numero final menos 1
for numero in range(1, 10):
	print(numero)

#é possivel tambbém mudar o incremento, que por padrão é 1, porem no exemplo temos que mudando o terceiro parametro é possivel mudar o incremento
# é importante notar que neste caso o primeiro parametro é obrigatório
for numero in range(0, 10, 2):
		print(numero)

# é possivel também mudar o range para decrescente da seguinte forma
# porém dependendo da situação é nescessário fazer alterações
for numero in range(9, -1, -1):
	print(numero)




