#Which starting number, under one million, produces the longest Colletz chain?
#next member in the chain n -> if n even then n/2 else 3n+1

'''
Idea: Make a array of 100000 zeros and fill in on the ith place the length of the collatz starting with number i.
- When you have a sequence fill in immediately the collatz number of the numbers in the sequence
- If during the the collatz sequence you encouter an number that has a collatz number you can stop
'''

def main():
  n=1000000
  numbers = [0 for i in range(n+1)]
  for i in range(1,n):
    colnum = i
    colseq = [colnum]
    val = True
    # print('next')
    while val:
      # See if the sequence is done
      if colnum == 1:
        for k in range(len(colseq)):
          if colseq[k] < n:
            numbers[colseq[k]] = len(colseq)-k
        val = False
      # See if there is already an collatz number known for colnum if so we are done and can complete the array
      elif colnum < n and numbers[colnum] != 0:
        for k in range(len(colseq)):
          if colseq[k] < n:
            numbers[colseq[k]] = len(colseq)+numbers[colnum]-k-1
        val = False
      # See what the next Collatz number is.
      else:
        colnum = next_Collatz(colnum)
        colseq.append(colnum)
  
  # Find the maximum in the array of collatz numbers
  max = 0
  index = 0
  for i in range(len(numbers)):
    if numbers[i] > max:
      max, index = numbers[i], i
  print(index)   

# Function to generate the next collatz number.
def next_Collatz(n):
  if n%2 == 0:
    return int(n/2)
  else:
    return int(3*n+1)

main()  