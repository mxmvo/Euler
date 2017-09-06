def main():
  n=1000000
  numbers = [0 for i in range(n+1)]
  for i in range(1,n):
    colnum = i
    colseq = [colnum]
    val = True
    # print('next')
    while val:
      # print(colnum,end=" ")
      if colnum == 1:
        for k in range(len(colseq)):
          if colseq[k] < n:
            numbers[colseq[k]] = len(colseq)-k
        val = False
      elif colnum < n and numbers[colnum] != 0:
        for k in range(len(colseq)):
          if colseq[k] < n:
            numbers[colseq[k]] = len(colseq)+numbers[colnum]-k-1
        val = False
      else:
        colnum = next_Collatz(colnum)
        colseq.append(colnum)
  print('\n')
  max = 0
  index = 0
  for i in range(len(numbers)):
    if numbers[i] > max:
      max, index = numbers[i], i
  print(index)

      
    




def next_Collatz(n):
  if n%2 == 0:
    return int(n/2)
  else:
    return int(3*n+1)



main()  