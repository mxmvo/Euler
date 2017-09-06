#! /usr/bin/python
import math
def main():
  file=open('/Users/maximoldenbeek/Documents/Code/Euler/euler67.txt','r')
  file = file.readlines()
  

  i = 2
  linebelow = [int(j) for j in file[-1].strip().split(" ")]
  
  while i<101:
    line = [int(j) for j in file[-1*i].strip().split(" ")]
    for j in range(len(line)):
      #print(len(linebelow),len(line),j)
      line[j] = line[j]+max(linebelow[j],linebelow[j+1])
    linebelow = line
    i+=1

  print(linebelow)

def pell(x ,y, d):
  return x**2-d*y**2

def fraction (num):  
  history = [1]
  regfract = []
  m = 0
  d = 1
  a0 = int(num**.5)
  a = a0
  regfract.append(a)
  history.append([a,d,m])
  temp =True
  while temp:
    m = d * a - m
    d = (num - m**2) / d
    a = int((a0+m)/d)
    if [a,d,m] in history:
      temp = False
    else:
      history.append([a,d,m])
      regfract.append(a) 
  return regfract  


def square(num):
  for i in range(int(num**.5-2),int(num**.5+2)):
    if i**2==num:
      return True
  return False


    



def primeFactor(num):
  arr = []
  d = 2
  while d**2 < num:
    if num%d == 0:
      num = num/d
      arr.append(d)
    else:
      d += 1
  return arr



def isGoldbach(num):
  for i in primesList(num):
    for j in range(1,int(num**.5)):
      if num == i + 2*j**2:
        return True
  return False
  
def isCompOdd(num):
  if num%2 == 0:
    return False
  for i in range (3,num,2):
    if num % i == 0:
      return True
  return False

def powset2(seq):
    result = []
    if seq:
        head, tail = seq[:1], seq[1:]
        for smaller in powset2(tail):
            result.append(smaller)
            result.append(head + smaller)
    else:
        result.append([])
    return result


def isPan(num):
    z = str(num)
    for i in range(1,len(z)+1):
      y = str(i)
      if y not in list(z):
        return False
    return True

def isPrime(num):
  if num%2 == 0:
    return False
  for i in range (3,int(math.sqrt(num))+1,2):
    if num%i==0:
        return False
  return True


def primesList(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = [True]*n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[2*i::i] = [False]*(len(sieve[2*i::i]))
    return [2]+[i for i in range(3,n,2) if sieve[i]]
main()