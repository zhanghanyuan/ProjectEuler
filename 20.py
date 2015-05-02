import math
s = str(math.factorial(100))
ans = 0
for i in s:
    ans += ord(i)-ord('0')
print ans
