import math

'''
So you can go right or down. In total you need to go 20 times right and 20 times down.
This can be done in 40!/(20!20!) different ways.
'''

print(math.factorial(40)/(math.factorial(20)**2))