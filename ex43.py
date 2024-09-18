#usuario digita o valor
peso = float (input('Digite Seu Peso (KG) '))
altura = float (input('Digite Seu Peso (M) '))
#descobrindo indice de massa corporia
imc = peso / (altura ** 2 )

#condiçoes


print ('Índice de Massa Corporal (IMC) é De: {:.1f}'.format(imc))
if imc < 18.5:
    print ('Você Está ABAIXO do PESO')
#condiçoes 'entre'
elif imc <= 18.5 and imc < 25:
    print ('Você Está Com o Peso Ideal')
elif imc <= 25 and imc < 30:
    print ('Você Está com SOBRE PESO')
elif imc <= 30 and imc < 40:
    print ('Você Está Com OBESIDADE')
else:
    print ('Você Está com OBESIDADE MORBIDA, Cuidado !')

#final do programa