n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))
n3: int = int(input('digite mais um numero:'))
menor = n1
if n2 < menor and n2 < n3:
    menor = n2
if n3 < menor and n3 < n2:
    menor = n3
maior = n1
if n2 > maior and n2 > n3:
    maior = n2
if n3 > maior and n3 > n2:
    maior = n3
print('menor valor digitado foi {}'''.format(menor))
print('maior valor digitado foi {}'.format(maior))

