kmL = float(input('Digite a quantidade de Km percorridos: '))
daysL = float(input('Digite a quantidade de dias alugado: '))
price = (kmL * 0.15) + (daysL * 60)
print('O valor a ser pago para a locadora é de: {:.2f}R$'.format(price))
#Concluido