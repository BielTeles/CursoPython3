import math
ang = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O angulo {} tem:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(ang, seno, cosseno, tangente))
#Concluido