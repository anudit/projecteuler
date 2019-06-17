"""

@link = https://projecteuler.net/problem=1
@author = https://github.com/anuditnagar

"""

def compute(r):
	ans = sum(x for x in range(r) if (x % 3 == 0 or x % 5 == 0))
	return ans

print(compute(1000))
