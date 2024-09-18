r1 = float (input ('Primeiro Segmento: '))
r2 = float (input ('Segundo Segmento:  '))
r3 = float (input ('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    print ('Os Segmentos acima PODEM formar um TRIANGULO! ')
    print('-' * 15)

  # CONDIÇOES
    if r1 == r2 == r3:
     print ('É Possivel Formar um Triangulo EQUILÁTERO')
    elif r1 != r2 != r3 != r1:

        print ('É Possivel Formar Um Triangulo ESCALENO')
    else:
        print ('É Possivel Formar Um Triangulo ISÓCELES')
else:
    print ('Os Segmentos NÃO PODEM Formar Um Triangulo! ')
