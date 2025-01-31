import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
aux = pow(co,2) + pow(ca,2)
hip = math.sqrt(aux)
print('A hipotenusa mede: {:.2f}'.format(hip))
#Concluido

#hi = math.hypot(co, ca) #calculo da hipotenusa!