n = str (input('Digite um Valor: '))

print ('''escolha uma base para conversão:
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opçao = int (input('Digite sua Opção '))

if opçao == 1:

    print ('{}  CONVERTIDO PARA BINARIO é {}'.format(n, bin(n)))
elif opçao == 2:

    print ('{} Convertido para OCTAL é {}'.format(n, oct(n)))
elif opçao == 3:

    print('{} Convertido para hexadecimal é {}'.format(n, hex(n)))