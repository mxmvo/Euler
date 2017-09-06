
cycle = []
for d in range(2,1000):
  r = 1
  rem = []
  cyclenum = 0
  temp = True
  while temp == True:
   while 0 < r < d:
     r = r*10
  #  print(r//d,end="  ")
   r = r % d
  #  print(r)
   if r in rem:
     i = rem.index(r)
     cyclenum = len(rem)-i
     print(len(rem),i,r)
     temp = False
   else:
     rem.append(r)
  cycle.append([cyclenum,d])

print(max(cycle))