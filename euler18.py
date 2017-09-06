#! /usr/bin/python
# in the file is a traingle of numbers find biggest sum of all possible path from top to down.
# Paths go down either straight or one to the right. 
# See also problem 67
'''
Brute force will work but is not ellegant. 
Idea:
Go from bottom up. In the row above add the number underneath.
'''


import math
def main():
  file=open('euler18.txt','r')
  file = file.readlines()
  

  i = 2
  linebelow = [int(j) for j in file[-1].strip().split(" ")]
  # Add the highest adjacent nubmer to the current line.
  while i<16:
    line = [int(j) for j in file[-1*i].strip().split(" ")]
    for j in range(len(line)):
      line[j] = line[j]+max(linebelow[j],linebelow[j+1])
    linebelow = line
    i+=1
  # print the last line which is the top and now contains the highest sum.
  print(linebelow)

main()