"""

@link = https://projecteuler.net/problem=2
@author = https://github.com/anuditnagar

"""

def compute(r):
	ans = 0
	a = 1
	b = 2
	while a <= r:
		if a % 2 == 0:
			ans += a
		a, b = b, a + b
	return ans

print(compute(4000000))
