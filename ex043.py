print('\033[1;34m-=-' * 10)
print('\033[1;33m CALCULE  O  SEU  IMC ')
print('\033[1;34m-=-' * 10)

alt = (float(input('\033[1;36mQual é a sua altura? (em metro): ')))
pêso = (float(input('Qual é o seu peso? (em kg): ')))
imc = pêso / (alt * alt)
print('O seu imc é {:.2f}'.format(imc))

if imc <= 18.5:
    print('Classificação ABAIXO DO PESO!')
elif 18.5 <= imc <= 25:
    print('Parabéns, você está com o PESO IDEAL!')
elif 25 <= imc <= 30:
    print('Você está em SOBREPESO, pratique atividades físicas!')
elif 30 <= imc <= 40:
    print('Você está em OBESIDADE, Cuidado!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, procure um médico nutricionista!!')

