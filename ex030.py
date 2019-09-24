num = int(input('Digite um número qualquer para saber se é PAR ou IMPAR:'))
resultado = num % 2
if resultado == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é Impar!'.format(num))
    