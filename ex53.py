from datetime import date
total_maior = 0
total_menor = 0
atual = date.today().year
for c in range (1, 7):
    nascimento = int (input('Digite o Ano de Nascimento da {}° Pessoa: '.format(c)))
    idade = atual - nascimento
    if idade <= 18:
        total_maior += 1
    else:
        total_menor += 1
print ('Tivemos {} pessoas Maiores de Idade '.format(total_maior))
print ('Tivemos {} pessoas Menores de Idade'.format(total_menor))