#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuario
#tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuario
#venceu ou perdeu

import random
numpc = int(random.randint(0,5))
#print(numpc)
numusu = int(input('Escreva um número de 0 a 5: '))
if numpc == numusu:
    print('Você acertou o número!')
else:
    print('Você errou o número! Era {}!'.format(numpc))
#Concluido