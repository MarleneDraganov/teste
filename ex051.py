primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão

for c in range(primeiro, décimo + 1, razão):
    print('{}'.format(c), end=' ')
print('ACABOU')
