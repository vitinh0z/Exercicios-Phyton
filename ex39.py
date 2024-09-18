from datetime import date
atual = date.today().year

# ANO DE NASCIMENTO + DESCOBRINDO IDADE
nasc = int (input('Ano de Nascimento: '))
idade = atual - nasc

print ('Quem Nasceu em {} Tem {} Anos em {}'.format(nasc, idade, atual))
print ('-' * 15)

if idade == 18:
    print ('Você Tem que se Alistar Imediatamente!')

elif idade < 18:
    saldo = 18 - idade
    print ('Ainda Faltam {} Ano(s) para o Seu Alistamento'.format(saldo))

elif idade > 18:
    saldo = idade - 18
    print ('Você ja Deveria Ter se Alistado há {} ano(s)'.format(saldo))
 