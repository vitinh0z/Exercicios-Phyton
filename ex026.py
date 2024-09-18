frase = str (input('Digite uma Frase: ')).upper().strip()
print('A Letra A apareceu {} vezes na frase'.format(frase.count('A')))
print('A Primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A Ultima Letra A apareceu na posiçao {}'.format(frase.rfind('A')+1))