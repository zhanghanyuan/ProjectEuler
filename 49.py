def isPrime(n):
    if n <= 1:
	return False
    for i in xrange(2,int(n ** 0.5)+1):
	if n % i == 0:
	    return False
    return True
def isSame(a,b):
    d = [0 for i in xrange(10)]
    x = str(a)
    for i in x:
	d[ord(i)-ord('0')] += 1
    y = str(b)
    for i in y:
	d[ord(i)-ord('0')] -= 1
    for i in xrange(10):
	if d[i] != 0:
	   return False
    return True    
for i in xrange(1000,10000):
    if isPrime(i):
	for j in xrange(1,5000):
	    if isPrime(i+j) and isPrime(i+2*j):
		if isSame(i,i+j) and isSame(i,i+2*j):
		    print str(i)+str(i+j)+str(i+2*j)
		    break

