#Desenvolva um programa que pergunte a distância de uma viagem em Km
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200km e R$0,45 para viagens mais longas
dist = float(input('Digite a distância de sua viagem em Km: '))
if dist <= 200:
    print('O valor da passagem é: R${:.2f}!'.format(dist*0.50))
else:
    print('O valor da passagem é: R${:.2f}!'.format(dist*0.45))
#Concluido