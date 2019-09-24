frase = str(input('Digite uma frse:')).upper().strip()
print('A letra A aparece {} vezes na frase'. format(frase.count('A')))
print('A letra A aparece pela primeira vez na frase na posição {}'.format(frase.find('A')+1))
print('A letra A aparece por último na frase na posição {}'.format(frase.rfind('A')+1))