pri = int (input('Primeiro Termo: '))
razão = int (input('Razão: '))
decimo = pri + (10 - 1) * razão
for c in range (pri, decimo + razão, razão):
    print (' {} '.format(c), end=' ')