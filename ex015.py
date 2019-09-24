km = float(input('Quantos km foi percorrido?'))
dias = float(input('O carro foi alugado por quantos dias?'))
valor = (60 * dias) + (0.15 * km)
print('Com o percusso de {} km e o carro alugado por {:.0f} dias o valor a pagar é:R$ {:.2f}'.format(km, dias, valor))