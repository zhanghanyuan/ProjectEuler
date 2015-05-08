def isPrime(n):
    if n <= 1:
	return False
    for i in xrange(2,int(n ** 0.5)+1):
	if n % i == 0:
	    return False
    return True
limit = 10 ** 6
ans = 0
for i in xrange(2,limit):
    l = len(str(i))
    w = i
    flag = True
    for j in xrange(l):
	if not isPrime(w):
	    flag = False
	    break	
	w = (w % 10) * (10 ** (l-1)) + w / 10
    if flag == True:
	ans += 1
print ans
