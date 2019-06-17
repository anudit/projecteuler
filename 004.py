"""

@link = https://projecteuler.net/problem=4
@author = https://github.com/anuditnagar

"""

def compute():
    ans=[]
    for i in range(100, 1000):
        for j in range(100, 1000):
            num= i*j
            if (str(num) == str(num)[::-1]):
                ans.append(num)

    ans = max(ans)
    return str(ans)

print(compute())
