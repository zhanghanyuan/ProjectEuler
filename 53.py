limit = 10 ** 6 + 1
d = [[0 for col in xrange(101)] for row in xrange(101)]
d[1][0] = d[1][1] = 1
for i in xrange(2,101):
    d[i][0] = 1
    for j in xrange(1,i+1):
	d[i][j] = d[i-1][j]+d[i-1][j-1]
	if d[i][j] >= limit:
	   d[i][j] = limit
ans = 0
for i in xrange(101):
    for j in xrange(i+1):
	if d[i][j] >= limit:
	    ans += 1
print ans

