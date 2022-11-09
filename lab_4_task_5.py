def area(a):
  if a == 'треугольник':
    h = int(input('введите h '))
    a = int(input('введите a '))
    print((h*a)/2)
  if a == 'круг':
    pi = int(input('введите pi '))
    r = int(input('введите r '))
    print(pi*r**2)
  if a == 'прямоугольник':
    a = int(input('введите a '))
    b = int(input('введите b '))
    print(a*b)
area('треугольник')