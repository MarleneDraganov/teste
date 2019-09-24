frase = str(input('Escreva uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print('O inverso de {} e {}'.format(junto, inverso))

if junto == inverso:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um Palímedro')