from random import randint

items = ('Pedra', 'Papel', 'Tesoura' )
computador = randint (0, 2)

print (''' Digite sua Escolha Com Sabedoria 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int (input ('Qual Sua Jogada:? '))

print ('-=' * 15)

print (' Computador Jogou {}'.format(items[computador]))
print (' Você jogou {}'.format(items[jogador]))
print ('-=' * 15)


if computador == 0: #pedra
    if jogador == 0:
        print ('Deu Empate')

    elif jogador == 1:
        print (' Você Perdeu')

    elif jogador == 2:
        print ('Você Ganhou')

    else:
        print ('Opção Invalida')

elif computador == 1: # papel
    if jogador == 0:
        print ('Deu Empate')

    elif jogador == 1:
        print ('Você Perdeu')

    elif jogador == 2:
        print ('Você Ganhou')
        
    else:
        print ('Opção Invalida')


elif computador == 2: #tesoura
    if jogador == 2:
        print ('Deu Empate')

    elif jogador == 1:
        print ('Você Perdeu')

    elif jogador == 2:
        print ('Você Ganhou')

    else:
        print ('Opção Invalida')
