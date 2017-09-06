import math

#Goal: Find the first triangle nubmer that has over 500 divisors

def main():
  # note the nth traingle number is n(n+1)/2
  # n and n+1 are relative prime so the only common divisor is 1.   
  n=1
  current = 1
  follow = 2

  while ((current-1)*(follow-1)) < 501:
    n += 1
    current, follow = follow, numdiv(int(n+1))
    print(n, current, follow , flush=True)
  print(n) 


# Calculate the number of divisors for a number n
def numdiv(n):
  j=0
  for i in range(1,int(n**.5)):
    if n%i==0:
      j+=2
    if int(n**.5)**2 == n:
      j -= 1
  return j

main()


