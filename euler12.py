import math

def main():
  n=1
  i=1
  current = 1
  follow = 2

  while ((current-1)*(follow-1)) < 501:
    n += 1
    current, follow = follow, numdiv(int(n+1))
    print(n, current, follow , flush=True)
  print(n) 

def numdiv(n):
  j=0
  for i in range(1,int(n**.5)):
    if n%i==0:
      j+=2
    if int(n**.5)**2 == n:
      j -= 1
  return j

main()
#print(numdiv(5984*5985/2))

