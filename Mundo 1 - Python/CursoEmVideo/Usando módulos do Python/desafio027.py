n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome: {}\n Seu ultimo nome: {}'.format(nome[0], nome[len(nome)-1]))
#Concluido