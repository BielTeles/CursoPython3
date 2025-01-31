#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO
cidade = str(input('Digite o nome da sua cidade: '))
cidade = cidade.upper()
cidDiv = cidade.split()
ver = cidDiv[0].find('SANTO')
print((cidDiv[0]))
if ver == -1:
    print('Não começa com Santo')

else:
    print('Começa com Santo')
#Concluido