import math
s = 0
def area(*args, **kw):
  if kw['figure'] == 'triangle':
    s = (args[0]/2) * args[1]
    print(s)
  elif kw['figure'] == 'circle':
    s = args[0]**2 * math.pi
    print(s)
  elif kw['figure'] == 'rectangle':
    s = args[0] * args[1]
    print(s)
  else:
    print('none')
area(2, figure = 'circle')