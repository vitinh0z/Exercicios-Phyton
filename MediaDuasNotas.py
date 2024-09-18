n1 = float (input ('Digite a Primeira nota '))
n2 = float (input ('Digite a Segunda nota '))
m = (n1 + n2)/2
print ('Sua MEDIA foi de {:.1f}'.format(m))
if m >= 6.0:
    print('A sua media foi boa, Parabens!! ')
else:
    print ('Sua media foi baixa, Estude mais!! ')