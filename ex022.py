nome = str(input('Escreva o seu nome completo:')).strip()
print('Análise do seu nome:')
print('O seu nome em maiúsculo é {}'.format(nome.upper()))
print('O seu nome em minúsculo é {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))


