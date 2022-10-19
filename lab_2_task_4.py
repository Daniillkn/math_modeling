a = [1, 1]
b = int(input(''))
c = 0
d = 1
sum = 0
sum += a[c] + a[d]
a.append(sum)
for i in range(b-2):
  c+=1
  d+=1
  sum = (a[c] + a[d])
  a.append(sum)
  sum = 0
for i in a:
  print(i, end = ' ')