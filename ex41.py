from datetime import date
atual = date.today().year
nascimento = int (input('Digite O Ano De Nascimento: '))
idade = atual - nascimento
print ('o Atleta Tem {} Anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print ('Classificação: INFANTIL')
elif idade <= 19:
    print ('Classificaçâo: JUNIOR')
elif idade <= 25:
    print ('Classificaçâo: SÊNIOR')
else:
    print ('Classificaçâo: MASTER')