n = str (input('Digite seu nome completo: ')).upper().strip()
nome = n.split()
print ('Muito prazer em te conhecer {}'.format(n))
print ('Seu primeiro nome é {}'.format(nome[0]))
print ('Seu Ultimo nome é {}'.format(nome[len(nome)-1]))
