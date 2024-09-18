salario = float(input('Digite o salario do funcionario R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100 )
else:
    novo = salario + (salario * 10 / 100 )
print ('Quem Ganhava R${:.2f} Passa a Ganhar R${:.2f}'.format(salario, novo))