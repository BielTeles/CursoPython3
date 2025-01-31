#Faça um programa que leia um ano qualquer e mostre se ele é bissexto
ano = int(input('Digite um ano qualquer para saber se é bissexto: '))
if ano % 4 == 0: #etapa 1
    if ano % 100 == 0: # etapa 2
        if ano % 400 == 0: # etapa 3
            print('O ano é bissexto!') #etapa 4
        else:
            print('O ano não é bissexto!') #etapa 5
    else:
        print('O ano é bissexto!') #etapa 4
else: #etapa 5
    print('O ano não é bissexto')
#Concluido