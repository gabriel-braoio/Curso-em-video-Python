import math
catop = float(input('digite o cateto oposto:'))
catad = float(input('digite o cateto adjacente:'))
hipotenusa = math.hypot  (catop,catad)
print('a hipotenusa de {} e {} é {:.2f}'.format(catop,catad,hipotenusa))
