'''Importar toda a biblioteca math'''
import math
an = float(input('Digite seu angulo: '))
seno = math.sin(math.radians(an))
print('seum angulo {} e o seno {:.2f}'.format(an, seno))
coseno = math.cos(math.radians(an))
print('seu angulo {} e seu coseno{:.2f}'.format(an, coseno))
tangente = math.tan(math.radians(an))
print('seu angulo {} e seu tangente {:.2f}'.format(an, tangente))

'''Importa partes da biblioteca math'''
from  math import radians,sin,cos,tan
an = float(input('Digite seu angulo: '))
seno = sin (radians(an))
print('seu angulo {} e o seno{:.2f}'.format(an, seno))
coseno = cos(radians(an))
print('seu angulo {} e seu coseno {:.2f}'.format(an, coseno))
tangente = tan(radians(an))
print('seu angulo {} e seu tangente {:.2f}'.format(an, tangente))