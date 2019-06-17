"""

@link = https://projecteuler.net/problem=6
@author = https://github.com/anuditnagar

"""

def compute(n=100):
	s = sum(i for i in range(1, n + 1))
	s2 = sum(i**2 for i in range(1, n + 1))
	return (s**2 - s2)

print(compute(100))
