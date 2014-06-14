__author__ = 'dixon'
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
from math import sqrt

pp = 2
ep = [pp]
print(ep)
pp += 1
tp = [pp]
print(tp)
ss = [2]
while len(tp) < 10001:
    pp += ss[0]
    test = True
    sqrtpp = sqrt(pp)
    for a in tp:
        if a > sqrtpp: break
        if pp % a == 0:
            test = False
            break
    if test: tp.append(pp)
ep.reverse()
[tp.insert(0,a) for a in ep]
print(len(tp))
print(tp[-2])