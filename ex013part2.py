p = float (input('Digte um Valor de Um Produto: R$'))
d = int (input('Digite o Desconto: %'))
n = p - (p * d / 100)
print ('O Produto que custava R${} na promoção de {}% vai custar R${}'.format (p, d, n))