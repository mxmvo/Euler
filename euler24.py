from math import factorial

candidates = [i for i in range(0,10)]
perm_elem = []
index = 10**6-1

for j in range(9,-1,-1):
    n = int(index/factorial(j))
    print(n)
    perm_elem.append(str(candidates[n]))
    index -= n*factorial(j)
    del candidates[n]

solution = ''.join(perm_elem)

print(solution)