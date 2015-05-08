key = 0
ans = 0
for i in xrange(1,1000):
    if 1000 % i == 0:
	continue
    a = set([0])
    b = 1
    cnt = 0
    while not (b in a):
	cnt += 1
        a.add(b)
	if b >= i:
	    b %= i
	b *= 10
    if cnt > key:
	key = cnt
	ans = i
print ans
