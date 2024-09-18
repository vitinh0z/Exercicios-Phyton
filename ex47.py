soma = 0
cont = 0
for n in range (2, 501, 2):
    if n % 3 == 0:
        cont = cont + 1
        soma = soma + n
print('A Soma de todos os {} valores requisitados são {}'.format(cont, soma))