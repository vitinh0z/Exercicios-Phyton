a = float (input('Digite o Primeiro Segmento: '))
b = float (input('Digite o Segundo Segmento: '))
c = float (input('Digitr o Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('Os Segmentos PODEM formar um Triangulo')
else:
    print ('Os Segmentos NÃO PODEM formar um Triangulo')