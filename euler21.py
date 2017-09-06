

def primesList(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = [True]*n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[2*i::i] = [False]*(len(sieve[2*i::i]))
    return [2]+[i for i in range(3,n,2) if sieve[i]]

print(primesList(30))
