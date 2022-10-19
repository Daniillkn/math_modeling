a = int(input(''))
b = int(input(''))
c = int(input(''))
if a + b < c or a+c<b or b+c <a:
  print('Такой треугольник не существует')
elif a==b and a==c:
  print('Это равносторонний треугольник')
elif a==b or b==c or c==a:
  print('Это равнобедренный треугольник')