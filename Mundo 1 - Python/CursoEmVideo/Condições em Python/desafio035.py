#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
#Verificando existencia
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possivel ser formado um triangulo!')
else:
    print('Não é possivel ser formado um triangulo!')
#Concluido