a = int (input('Digite Um Valor: '))
b = int (input('Digite Um Segundo Valor: '))
c = int (input('Digite um Terceiro Valor: '))

# Verficando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c > a and c > c:
    menor = c

# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

# Mensagem de Finalização
print ('O menor Valor Digitado Foi {}'.format(menor))

print ('O maior Valor Digitado Foi {}'.format(maior))