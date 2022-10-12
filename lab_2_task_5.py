a = int(input(''))
b = int(input(''))
if a%b == 0 and b != 0:
  print('Yes')
  print(a / b)
else:
  print('No')
  print(a - b)
  print(a//b)