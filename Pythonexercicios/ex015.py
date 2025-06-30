kmp = float(input('quantos km voce percorreu com o carro:'))
dca = float(input('quantos dias o carro foi alugado:'))
pd = dca*60
pkm = kmp*0.15
total = pd + pkm
print ('o valor que voce vai pagar por km rodado é {} e o dias de aluguel é {} o total dos dois é {}'.format(pkm,pd,total))