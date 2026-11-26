import math

def factorial(n):
    nums = [num for num in range(1,n+1)]
    total = 1
    for element in nums:
        total *= element
    return total

def brocard():
    n = 1
    count = 0
    while n<=1000:
        if math.isqrt(factorial(n)+1)**2 == factorial(n)+1: 
            count += 1
        n += 1      
    return count

print(brocard())