from datetime import date
ano = float(input('qual ano vamos ver? se colocar 0 vai analisar o ano atual'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano %100 != 0 or ano % 400 == 0:
    print('ano bissexto')
else:
    print('ano normal')