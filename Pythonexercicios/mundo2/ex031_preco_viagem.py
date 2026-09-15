kmvi = float(input('quantos km tem sua viagem:'))
if kmvi <= 200:
    menor = kmvi* 0.30
    print('o preço da sua viagem vai ser esse {:.2f}'.format(menor))
else:
    maior = kmvi * 0.45
    print('o preço da sua viagem vai ser esse {:.2f}'.format(maior))
