num = int (input ('Digite um Número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print ('\033[34m',end='')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print ('{}'.format(c), end=' ')

print ('\n\033 O número {} foi divisivel {} vez(s)'.format(num, tot))
if tot == 2:
    print ('E Por isso Ele É PRIMO')
else:
    print ('E por isso ele NÃO É PRIMO')