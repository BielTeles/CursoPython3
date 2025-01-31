#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece: {}'.format(frase.count('A')))
print('A letra A aparece pela primeira vez: {}'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez: {}'.format(frase.rfind('A')+1))
#Concluido