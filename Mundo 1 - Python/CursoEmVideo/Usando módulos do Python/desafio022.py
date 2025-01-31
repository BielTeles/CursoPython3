#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas minusculas
#Quantas letras ao total (sem espaço)
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
nomeUpper = nome.upper()
nomeLower = nome.lower()
nomeDiv = nome.split()

#qtdlts = ''.join(nomeDiv)
#print((len(nomeDiv[0]))+(len(nomeDiv[1])))
#print(len(nomeDiv[0]))

print('O nome com todas as letras maiusculas: {}'.format(nomeUpper))
print('O nome com todas as letras minusculas: {}'.format(nomeLower))
print('Quantidade de letras sem espaços: {}'.format((len(nomeDiv[0]))+(len(nomeDiv[1]))))
print('Quantidade de letras do primeiro nome: {}'.format(len(nomeDiv[0])))
#Concluido