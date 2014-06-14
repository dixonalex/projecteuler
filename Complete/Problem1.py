__author__ = 'alexdixon'
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def lesserThanCheck(x,limit):  # x is the number you're checking for multiples, limit is the upper limit (1000 here)
    i = 1
    isLesser = True
    myArray = []
    while isLesser:
        multiple = x * i
        if multiple >= limit:
            return(sum(myArray))
        else:
            myArray.insert(i,multiple)
            i += 1

print(lesserThanCheck(3,1000) + lesserThanCheck(5,1000) - lesserThanCheck(15,1000))

# Using arithmetic progression formulae

def arithSolution(x,limit):
    return int((x*int(limit/x)*(1+int(limit/x)))/2)

print(arithSolution(3,1000) + arithSolution(5,1000) - arithSolution(15,1000))