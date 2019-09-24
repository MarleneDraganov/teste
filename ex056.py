soma = 0
mediaIdade = 0
nomeHomenVelho = ''
maiorIdadeHomen = 0
nasc =0
qtdMulherMenor20 =0 #aqui tera a soma das mulheres

for p in range(1, 5):
     print('==== {}ª pessoa:==== '.format(p))
     nome = (str(input('Qual é o seu Nome?:'))).upper()
     idade = (int(input('Qual é a sua idade?:')))
     sexo = (str(input('Sexo - F/M:'))).upper()
     soma = soma + idade

     if sexo == 'M' and idade > maiorIdadeHomen:
          maiorIdadeHomen += 1
          maiorIdadeHomen = idade
          nomeHomenVelho = nome

     if sexo == 'F' and idade < 20:
          qtdMulherMenor20 += 1

mediaIdade = soma / 4


print('A média de idade do grupo analisado é de {} anos.'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadeHomen, nomeHomenVelho))
print('Há {} mulhere(s) com menos de 20 anos.'.format(qtdMulherMenor20))





