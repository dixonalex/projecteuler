__author__ = 'dixon'
'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def squareSum(x):
    b=0
    for a in range(1,x+1):
        b += a**2
        if a == x: return(b)

def sumSquare(x):
    b=0
    for a in range(1,x+1):
        b += a
        if a== x: return(b**2)

ans = int(input("Find the difference between the sum of the squares and the square of the sum of which natural number: "))
print(sumSquare(ans) - squareSum(ans))

#Arithmetic approach
limit = 100
sum = limit*(limit + 1)/2
sum_sq = (2*limit + 1)*(limit + 1)*limit/6
print(sum**2 - sum_sq)