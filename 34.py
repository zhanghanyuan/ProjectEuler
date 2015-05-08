import math
limit = 5 * (10 ** 6)
ans = 0
for i in xrange(3,limit):
    s = str(i)
    sum = 0
    for j in s:
	sum += math.factorial(ord(j)-ord('0'))
    if sum == i:
	ans += i 
print ans
