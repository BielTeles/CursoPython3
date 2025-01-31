#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#Para salarios superiores a 1250,00 calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

sal = float(input('Escreva seu salario: '))
if sal > 1250.00:
    print('Seu novo salario é: {:.2f}'.format(sal + (sal*0.1)))
else:
    print('Seu novo salario é: {:.2f}'.format(sal + (sal*0.15)))
#Concluido