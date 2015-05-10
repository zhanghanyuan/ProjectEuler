mod = 10 ** 10
ans = 0
for i in xrange(1,1001):
    w = i
    for j in xrange(i-1):	
	w = w * i % mod 
    ans = (ans + w) % mod
print ans
