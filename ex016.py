dias = int (input('Quantos dias alugados: '))
km = float (input('Quantos KM rodados: '))
p = (dias * 60) + (km + 0.15)
print ('O Total a pagar sera de R${:.2f}'.format (p))