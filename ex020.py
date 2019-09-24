from random import shuffle
n1 = str(input('primeiro nome:'))
n2 = str(input('Segundo nome:'))
n3 = str(input('Terceiro Nome:'))
n4 = str(input('Quarto nome:'))
lista= [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação dos trabalhos será:')
print(lista)