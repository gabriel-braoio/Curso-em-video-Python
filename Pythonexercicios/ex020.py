import random
n1 = str(input('digite um aluno:'))
n2 = str(input('digite um aluno:'))
n3 = str(input('digite um aluno:'))
n4 = str(input('digite um aluno:'))
list = [n1,n2,n3,n4]
random.shuffle(list)
print ('a ordem para apresentaçao dos trabalhos é {}'.format(list))