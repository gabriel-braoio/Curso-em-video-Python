sal = float(input('qual seu salario:'))
if sal >= 1250:
    aumedez = (sal*0.10) + sal
    print('seu salario com aumento de 10% é {}'.format(aumedez))
else:
    aumequinze = (sal*0.15)+sal
    print('seu salario com aumento de 15% é {}'.format(aumequinze))