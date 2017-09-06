import math

def main():
  primes = primesList(28123)
  abundantlist = []
  for i in range(2,28123):
    if sumOfFactors(i,primes) > i:
      abundantlist.append(i)
  sumlist = [False]*28124
  for i in range(len(abundantlist)):
    for j in range (i,len(abundantlist)):
      if (abundantlist[i]+abundantlist[j])< len(sumlist):
        sumlist[abundantlist[i]+abundantlist[j]] = True
  filt = [i for i in range(28124) if sumlist[i] == False]
  print(sum(filt))
           
  


def primesList(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = [True]*n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[2*i::i] = [False]*(len(sieve[2*i::i]))
    return [2]+[i for i in range(3,n,2) if sieve[i]]

def sumOfFactors(n, primes):
  num = n
  sum = 1
  i = 0
  while n > 1:
    p = primes[i]
    j = 0
    while n % p == 0:
      j += 1
      n = n / p 
    i += 1
    sum *= (p**(j+1)-1)/(p-1) 
  return int(sum - num)
main()
