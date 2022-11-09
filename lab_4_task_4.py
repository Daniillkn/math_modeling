def func(a, b):
  y = 1
  list = []
  for x in range(a, b+1):
    y = x**2
    list.append(y)
  print(list)
func(1, 4)