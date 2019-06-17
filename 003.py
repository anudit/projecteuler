
"""

@link = https://projecteuler.net/problem=3
@author = https://github.com/anuditnagar

"""

import math
def smallest_prime_factor(n):
	assert n >= 2
	for i in range(2, int(math.sqrt(n) + 1)):
		if n % i == 0:
			return i
	return n

def compute(n):
	while True:
		p = smallest_prime_factor(n)
		if p < n:
			n //= p
		else:
			return str(n)

print(compute(600851475143))
