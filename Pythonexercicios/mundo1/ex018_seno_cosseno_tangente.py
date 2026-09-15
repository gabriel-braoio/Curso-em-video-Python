import math
ang = float(input('digite um angulo:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('o angulo é {} e seu seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(ang,sen,cos,tan))