re1 = float(input('qual é tamanho da reta 1'))
re2 = float(input('qual é tamanho da reta 2'))
re3 = float(input('qual é tamanho da reta 3'))
if re1 < re2 + re3 and re2 < re1 + re3 and re3 < re1 +re2:
    print('é possivel formar um triangulo')
else:
    print('nao é possivel formar um triangulo')