num = int (input('Digite um Número para ver sua tabuada: '))
for c in range (1, 11):
    print('{} X {:.1f} = {}'.format(num, c, num*c))