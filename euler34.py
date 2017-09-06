import math

digit_fact = dict((str(n),math.factorial(n))  for n in range(10))

def sumfactorials(n):
  tot = 0
  for i in str(n):
    tot+= digit_fact[str(i)]
  return tot

total = 0
for k in range(10000000):
  if k == sumfactorials(k):
    total += k

print(total)
