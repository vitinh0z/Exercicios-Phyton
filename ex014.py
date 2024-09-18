s = float (input('Digite o Salario do Funcionario R$'))
a = int (input('Digite a porcentagem de aumento %'  ))
d = s + (a * s / 100)
print ('O salario do Funcionario que era de R${:.2f}, com o aumento de {:.2f}%, será de R${:.2f}'.format (s, a, d))