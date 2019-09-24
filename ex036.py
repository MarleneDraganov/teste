print('\033[1;34m==========AVALIADOR DE EMPRÉSTIMO IMOBÍLIÁRIO============')
casa = float(input('\033[1;36mQual é o valor da casa? R$ '))
salário = float(input('Qual é o salário do Comprador? R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para comprar uma casa de R$ {} em {} anos'.format(casa, anos))
print('a prestação será de R$ {:.2f}'.format(prestação))
if prestação <= mínimo:
    print('O emprestimo pode ser CONCEDIDO !')
else:
    print('Empréstimo NEGADO! ')

