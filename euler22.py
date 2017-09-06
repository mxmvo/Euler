
def temp(n):
  return int(ord(n)-64)

file = open('euler22.txt','r')

file= file.read()

file = file.split(",")

for i in range(len(file)):
  file[i] = file[i].strip('"\n')

file.sort()
total = 0

for i in range(len(file)):
  total += sum(map(temp,list(file[i]))) * (i+1)

print(total)