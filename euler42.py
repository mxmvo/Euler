triagnum = [int(.5*n*(n+1)) for n in range(1,50)]
print(triagnum)


file = open('euler42.txt','r')

file = file.readlines()

file = file[0].strip('"')
wordlist = file.split('","')


def triagvalue(string):
  value = 0
  for i in string:
    value += ord(i) - 64
  return value

total = 0
for i in wordlist:
  if triagvalue(i) in triagnum:
    total +=1

print(total)