#Evaluate the sum of all the amicable numbers under 10000.


def main():
    n=10000
    array = [0 for i in range(10000)]
    for i in range(1,10000):
        if array[i]==0:
            #Check if the numbers are Amicable. If so put them in the array
            if i == sumdiv(sumdiv(i)) and i != sumdiv(i):
                 array[i]=i
                 array[sumdiv(i)]=sumdiv(i)
    # Calculate as the question specifies.
    print(sum(array))
    
# Calculate the sum of the proper divisors. Only works for natural numbers inlcuding 0
def sumdiv(n):
    # special case for 1 and 0
    if n<=1:
        return 0
    else:
        j = 0
        for i in range(2, int(n**.5)+1):
            if n%i == 0:
                j += i+n//i
        if int(n**0.5)**2 == n:
            j-=int(n**0.5)
        return j+1

main()
