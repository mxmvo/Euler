#! /usr/bin/python
import math
def main():
  file=open('euler18.txt','r')
  file = file.readlines()
  

  i = 2
  linebelow = [int(j) for j in file[-1].strip().split(" ")]
  
  while i<16:
    line = [int(j) for j in file[-1*i].strip().split(" ")]
    for j in range(len(line)):
      #print(len(linebelow),len(line),j)
      line[j] = line[j]+max(linebelow[j],linebelow[j+1])
    linebelow = line
    i+=1

  print(linebelow)

main()