distancia = float(input('Qual é a distancia da sua viagem?:'))
print('Você está prestes a fazer uma viagem de {}km'.format(distancia))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('O valor da sua passagem é R${:.2f}'.format(valor))
