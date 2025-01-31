#crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome
nome = str(input('Digite seu nome: '))
nome = nome.upper()
ver = nome.find('SILVA')
if ver == -1:
    print('Não tem SILVA no nome')
else:
    print('Tem SILVA no nome')
#Concluido