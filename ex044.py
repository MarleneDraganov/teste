print('*' * 35)
print('{:=^35}'.format('     DRAGANOV  STORE     '))
print('*' * 35)
preço = float(input('Preço das Compras:R$ '))

print('''FORMA DE PAGAMENTO 
[1] à vista dinheiro/cheque
[2] á vista no cartão
[3] 2 X no cartão
[4] 3 ou mais vezes no cartão''')
opção = int(input('Qual é a sua opção?: '))
if opção == 1:
    total = preço -(preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('Sua compra será em duas parcelas de R$ {:.2f} sem juros'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Em quantas parcelas?:'))
    parcela = total / totparc
    print('A sua compra será parcelada em {} X de R$ {:.2f} com juros'.format(totparc, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')



print('Sua compra de R$ {:.2f} vai custar R$ {}'.format(preço, total))


