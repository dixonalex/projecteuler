__author__ = 'alexdixon'

max = 999**2
range = range(100, 999)
divisors = [0]

num = max
while num > 10000:
    if str(num)[::-1] == str(num):
        for a in range:
            if num % a == 0:
                divisors.append(a)
                if num == (divisors[-1] * divisors[-2]):
                    print(num)
                    print(divisors[-1],divisors[-2])
                    exit()
        num -= 1
    else: num -= 1
print(divisors)