import itertools
def isPrime(n):
    if n <= 1:
	return False
    for i in xrange(2,int(n ** 0.5)+1):
	if n % i == 0:
	    return False
    return True
ans = 0
for i in itertools.permutations("1234567",7):
    w = 0
    for j in i:
	w = w*10+ord(j)-ord('0')
    if isPrime(w) == True:
	ans = max(ans,w)
print ans
