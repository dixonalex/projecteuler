__author__ = 'dixon'
'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

num=600851475143
p=2
while (p<num):
    if num%p==0:
        num=num/p
    else:
        p=p+1
print(num)


'''from math import sqrt


print(int(sqrt(600851475143)))
pp = 2
ep = [pp]
pp += 1
tp = [pp]
print(tp)
ss = [2]
lim=sqrt(600851475143)
while pp < int(lim):
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
print(tp[-2])


i = -2
test = True
while test:
    if 600851475143 % tp[i] == 0:
        print(tp[i])
        test = False
        break
    if tp[i] < 0:
        test = False
        break
    else: i -= 1'''





