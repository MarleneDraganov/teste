velocidade = float(input('Qual é a velocidade atual do  carro?:'))
if velocidade > 80:
    print('MULTADO! Execedeu o limite máximo de velocidade!')
    multa = (velocidade - 80) * 7
    print('O valor da multa é R$ {:.2f}'.format(multa))
print('Tenha um Bom dia! Dirija sempre com segurança!')