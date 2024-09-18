from random import choice
n1 = str (input('Nome do(a) Primeiro(a) Aluno(a): '))
n2 = str (input('Nome do(a) Segundo(a) Aluno(a): '))
n3 = str (input('Nome do(a) Terceiro(a) Aluno(a): '))
n4 = str (input('Nome do(a) Quarto(a) Aluno(a): '))
l = [n1, n2, n3, n4]
escolhido = choice (l)
print ('O Escolhido foi {}'.format (escolhido))