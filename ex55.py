
somaidade = 0 
mediaidade = 0
maioridadehome = 0
nomevelho = ''
totmulher = 0
for pe in range (1, 5):
    print ('------- {}° PESSOA -------'.format(pe))
    nome =   str (input ('Qual é o Nome dessa Pessoa: '.format(pe))).strip
    idades = int (input ('Qual a Idade dessa Pessoa: '.format (pe)))
    sexo = (input ('Qual Sexo Dessa Pessoa?. Digite M Para Masculino / Digite F Para Feminino: ')).upper
    somaidade += idades
    if str (pe) == 1 and sexo in 'M':
        maioridadehome = idades
    nomevelho = nome
    if str (sexo) in 'M' and idades < maioridadehome:
        maioridadehome = idades
    nomevelho = nome
    if str (sexo) in  'F'  and int (idades) < 20:
        totmulher += 1
mediaidade = somaidade / 4
print ('A Media de Idade é {} Anos'.format(mediaidade))
print ('O Homem mais Velho tem {} Anos e Se Chama {}'.format(maioridadehome, nomevelho))
print ('Ao Todos são {} Mulheres com menos de 20 anos'.format(totmulher))