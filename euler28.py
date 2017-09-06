

i = 1
tot = 1
j = 1

for m in range(500):
  i += 1
  i += j
  tot += i
  j += 1
  for n in range(3):
    i += j
    tot += i
  j+=1

print(tot)