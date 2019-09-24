a = int(input('\033[1;35m Primeiro valor:'))
b = int(input('\033[1;35m Segundo valor:'))
c = int(input('\033[1;35m Terceiro valor:'))

# Verificanco o menor valor

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando o maior valor

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('\033[1;36m O menor valor digitado foi:{}'.format(menor))
print('\033[1;36m O maior valor digitado foi:{}'.format(maior))



