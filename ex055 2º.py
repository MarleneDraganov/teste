lista =[]
for p in range(1, 6):
    peso = float(input(' Digite o peso da {}ª pessoa:'.format(p)))
    lista += [peso]
print('O maior peso registrado foi {} Kg.'.format(max(lista)))
print('O menor peso registrado foi {} kg.'.format(min(lista)))
