print('\033[1;31m -=-' * 13)
print('\033[1;34m Analisador de Triângulos ')
print('\033[1;31m -=-' * 13)
r1 = float(input('\033[1;33m Primeiro Seguimento:'))
r2 = float(input('\033[1;33m Segundo Seguimento:'))
r3 = float(input('\033[1;33m Terceiro Seguimento:'))

# Para formar um triângulo é necessário que cada seguimento seja menor que a soma dos outros dois seguimentos.

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;34m Os Seguimentos acima PODEM formar um Triângulo.')
else:
    print('\033[1;34m Os Seguimentos acima NÃO podem formar um Triângulo,')


