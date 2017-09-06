

def isPalindrome(n):
  for i in range(int(len(str(n))/2)):
    if str(n)[i] != str(n)[int(-1*(i+1))]:
      return False
  return True

total = 0

for i in range(1000000):
  if isPalindrome(i) and isPalindrome(bin(i)[2:]):
    total += i

print(total)
