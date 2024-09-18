from math import hypot
a = float(input('Digite o Valor do Cateto Oposto: '))
b = float(input('Digite o valor do Cateto Adjacente: '))
hi = hypot(a, b)
print ('A Hipotenusa Vai Medir {:.2f} '.format(hi))