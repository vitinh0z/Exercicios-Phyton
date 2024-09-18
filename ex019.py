from math import sin, cos, tan, radians
a = float (input('Digite o Angulo que Você deseja: '))
s = sin(radians(a))
print ('O de ângulo de {} Tem o SENO de {:.2f}'.format(a, s))
c = cos(radians(a))
print ('Angulo de {} tem o COSSENO de {:.2f}'.format(a, c))
t = tan(radians(a))
print ('Angulo de {} tem o TANGENTE de {:.2f}'.format(a, t))