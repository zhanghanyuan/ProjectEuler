limit = 10 ** 6
vis = [1 for i in xrange(limit+1)]
d = []
def isPrime(n):
    if n <= 1:
	return False
    for i in xrange(2,int(n ** 0.5)+1):
	if n % i == 0:
	    return False
    return True
def seive(n):
    for i in xrange(2,n+1):
	if vis[i]:
	    d.append(i)
	for j in d:
	    if j * i > n:
		break
	    vis[j*i] = 0
	    if i % j == 0:
		break	    
seive(limit)
d.append(0)
l = len(d)
key = 0
ans = 0
for i in xrange(l-1):
    w = 0 
    t = i
    while t < l-1:
	w += d[t]
	if w > limit:
	   break
	if isPrime(w):
	   if key < t-i+1:
	       key = t-i+1
	       ans = w
	t += 1 
print ans
