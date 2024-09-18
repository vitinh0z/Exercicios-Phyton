velocidade = float(input('Qual era a velocidade do carro?:KM/h'))
if velocidade > 80:
    print('Multado! você execedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80)*7
    print('Valor da Multa sera de R${:.2f}'.format(multa))
print('Tenha um Bom Dia, Dirija com Cuidado')