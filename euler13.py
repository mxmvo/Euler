import math

file = open('euler13.txt','r')

file = file.readlines()
sum = 0
for i in file:
  sum += int(i)

print(str(sum)[0:10])
