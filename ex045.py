from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura', 'Inválida')
computador = randint(0, 2)
print('\033[1;33m-*-' * 10)
print('\033[1;36m{:=^30}'.format(' JOGO JOKEMPÔ '))
print('\033[1;33m-*-' * 10)
print('''\033[1;36mSuas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Qual é a sua jogada?: '))

print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PÔ!')
print('-=' * 12)
print(' Computador jogou {}'.format(itens[computador]))
print(' Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)

if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR GANHOU!')
    elif jogador == 2:
        print('COMPUTADOR GANHOU!')
    else:
        print(' JOGADA INVÁLIDA!')

elif computador == 1:
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 0:
        print('COMPUTADOR GANHOU!')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 0:
        print('JOGADOR GANHOU!')
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA')

