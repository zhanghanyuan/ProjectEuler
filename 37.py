def isPrime(n):
    if n <= 1:
	return False
    for i in xrange(2,int(n ** 0.5)+1):
	if n % i == 0:
	    return False
    return True
ans = 0
limit = 10 ** 6
for i in xrange(11,limit):
    l = len(str(i))
    flag = True
    for j in xrange(l):
	if not isPrime(int(str(i)[j:])) or not isPrime(int(str(i)[0:j+1])):
	    flag = False
    if flag == True:
	print i
	ans += i
print ans
