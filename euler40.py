
champernowne = '0'
for i in range(1,1000000):
  champernowne += str(i)

B = list(champernowne)
total = 1
for i in range(7):
  print(int(B[10**i]))
  total = total*int(B[10**i])
  print("total",total)

print(total)