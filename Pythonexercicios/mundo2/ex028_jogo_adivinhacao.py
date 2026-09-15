import random
sorte = random.randint(0,5)
print('vamos jogar um jogo ?, pensei em um numero tente adivinhar')
adv = int(input('qual é o numero ?'))
if sorte == adv:
    print('parabens')
else:
    print('o computador venceu')