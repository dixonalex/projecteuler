__author__ = 'dixon'
'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

pn = 25400000
chk = [11,12,13,14,15,16,17,18,19,20]

while pn < 254000000:
    for elem in chk:
        if pn % 19 == 0:
            if all(pn % a == 0 for a in chk): print(pn)
    else: pn += 20

