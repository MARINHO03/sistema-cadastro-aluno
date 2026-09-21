from math import radians, sin, cos, tan
angulo=float(input('escreva um ângulo:'))
seno=sin(radians(angulo))
print('o angulo de {} tem o seno de {:.2f}'.format(angulo,seno))
cosseno=cos(radians(angulo))
print('o angulo de {} tem cosseno de {:.2f}'.format(angulo,cosseno))
tangente= tan(radians(angulo))
print('o angulo de {} tem tangente de {:.2f}'.format(angulo,tangente))