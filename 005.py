"""

@link = https://projecteuler.net/problem=5
@author = https://github.com/anuditnagar

"""

import fractions

def compute():
	ans = 1
	for i in range(1, 21):
		ans *= i // fractions.gcd(i, ans)
	return ans

print(compute())
