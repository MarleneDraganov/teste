from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(' O ângulo de {} tem seno de {:.2f} cosseno de {:.2f} e tangente de {:.2f}'.format(angulo, seno, cosseno, tangente))