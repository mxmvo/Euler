

p = 120 
collect = []
for p in range(1001):
  i = 0
  for c in range(int(p/3),int(p/2+1)):
    for b in range(int(c/2),c):
      a = p - c - b
      if not a > b:
        if a**2+b**2 == c**2:
          i += 1
  collect.append([i,p])

print(max(collect))
