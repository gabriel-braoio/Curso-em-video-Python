vel: int = int(input('qual a sua velocidade?'))
if vel > 80:
    multa = (vel - 80) * 7
    print('voce recebeu uma multa e esse é o valor da multa {}'.format(multa))
print('Dirija em segurança tenha um bom dia')