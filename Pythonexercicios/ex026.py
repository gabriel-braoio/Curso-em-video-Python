frase = str(input('digite uma frase:')).strip()
print('a letra a aparece {} na frase'.format(frase.count('a')))
print('a primeira vez que a letra a aparece e na posicao {}'.format(frase.find('a')+1))
print('a ultima vez que a letra a aparece e na posicao {}'.format(frase.rfind('a')+1))
