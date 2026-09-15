import random
n1 = str(input('digite o nome do aluno'))
n2 = str(input ('digite o nome do aluno'))
n3 = str(input('digite o nome do aluno'))
n4 = str(input('digite o nome do aluno'))
lista= [n1,n2,n3,n4]
esc =random.choice(lista)
print ('o aluno escolhido foi {}'.format(esc))