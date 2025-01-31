#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cada km acima do limite

#import math
spd = float(input('Digite a velocidade do seu carro: '))
if spd > 80:
    multa = (spd - 80) * 7
    print('Você foi multado em R${:.2f} pelo excesso de velocidade!'.format(multa))
else:
    print('Você está dentro do limite de velocidade!')
#Concluido