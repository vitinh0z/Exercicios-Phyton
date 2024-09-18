from random import randint
cpu = randint(0, 5)  # faz o computador pensar em um numero

print('COMPUTADOR: Vou pensar em um numero entre 0 e 5, Duvido você advinhar....')
print ('-=-' * 20)

player = int (input('COMPUTADOR: Em que numero eu pensei?: ')) #Player tenta advinhar

if player == cpu:
   print ('PARABENS você consegiu me derrotar')

else:
    print ('HAHAHA eu ganhei, eu pensei no numero {} não no {}'.format(cpu, player))