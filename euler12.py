import math

#Goal: Find the first triangle nubmer that has over 500 divisors
'''
Say you want to find the devisors of x/2 for a number x.
Then notice you can write x=2^i*y where y is an odd number with k divisors. 
In fact k is the number of divisors of x divided by i+1 
Now the number of divisors for x are (i+1)*k and thus for x/2 is i*k = i/(i+1)*numdiv(x)
'''
def main():
  # note the nth traingle number is n(n+1)/2
  # n and n+1 are relative prime so the only common divisor is 1.   
  n=1
  # num div for 1
  current = 1
  # num div for 2 
  follow = 2
  notthere = True

  while notthere:
    n += 1
    current , follow = follow , numdiv(int(n+1))
    i = numtwos(current*follow)
    if (i)/(i+1)*current*follow > 500:
      notthere = False
  print(n*(n+1)/2)

# calculate the number of twos
def numtwos(n):
  j=0
  while n%2==0:
    j+=1
    n = n/2
  return j

# Calculate the number of divisors for a number n
def numdiv(n):
  j=0
  for i in range(1,int(n**.5)+1):
    if n%i==0:
      j+=2
  if int(n**.5)**2 == n:
    j -= 1
  return j

main()


