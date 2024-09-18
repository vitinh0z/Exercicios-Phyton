
peso_maior = 0
peso_menor = 0
for c in range (1, 6):
    peso = float (input ('Qual o Peso da {}° Pessoa?: '.format(c)))
    
    if c == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
           peso_menor = peso

print ('O Maior Peso Lido foi de {}Kg'.format(peso_maior))
print ('O Menor Peso Lido Foi de {}Kg'.format(peso_menor))