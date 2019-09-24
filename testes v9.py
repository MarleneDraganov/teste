nome = str(input('Digite o seu nome completo:')).strip()
print('Ola!!')
print('O seu nome em  maiúscilas é:{}'.format(nome.upper()))
print('O seu nome em minúsculas é: {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras.'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras!'.format(separa[0], len(separa[0])))



