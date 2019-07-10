"""

@link = https://projecteuler.net/problem=12
@author = https://github.com/anuditnagar

"""

from tqdm import tqdm
from math import sqrt
from functools import lru_cache

@lru_cache(maxsize=512)
def factors(n):
    return set(x for tup in ([i, n//i]
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

sum = 0
for num in tqdm(range(0, 13000)):
    tno  = sum
    factList = factors(tno)
    if(len(factList) >= 500):
        break
    sum +=num

print(sum)
