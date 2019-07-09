"""

@link = https://projecteuler.net/problem=7
@author = https://github.com/anuditnagar

"""

def prime(n):
    if n < 2:
        return False
    for i in range(2,int(pow(n, 1/2)) + 1):
        if n % i == 0:
            return False
    return True

sum = 0

for n in range(2000000):
    if prime(n):
        sum += n

print(sum)
