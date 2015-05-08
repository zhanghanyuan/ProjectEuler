def isPrime(n):
    if n <= 1:
	return False
    for i in xrange(2,int(n ** 0.5)+1):
    	if n % i == 0:
	    return False
    return True	
key = 0
ans = 0
for i in xrange(-999,1000):
    for j in xrange(-999,1000):
	k = 1
	while isPrime(k * k + i * k + j):
		k += 1
	if k > key:
	    key = k
	    ans = i * j
print ans
