casa = float (input('Qual o Valor da Casa?: R$'))
salario = float (input('Qual o Valor da Casa?: R$'))
anos = int (input('Quantos anos a Casa sera Financiada?: '))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print ('Para Pagar uma Casa de R${:.2f} em {} Anos, a prestação sera de R${:.2f} '.format(casa, anos, prestaçao))
if prestaçao <= minimo:
    print ('Emprestimo Pode ser CONCEDIDO')
else:
    print ('Emprestimo foi Negado')