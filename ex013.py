larg = float (input('Digite a Largura da Sua Parede '))
alt = float (input ('Digite a Altura da Sua Parede '))
a = larg * alt
print ('Sua Parede tem a dimensão de {}x{} e Sua Area é de {}m².'.format(larg, alt, a))
t = a / 2
print ('Para Pintar essa Parede, Você precisara de {}L de Tinta.'.format(t))