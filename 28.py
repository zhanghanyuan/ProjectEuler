a = 1
sum = 1
w = 0
for i in xrange(1001/2):
    w += 2
    for j in xrange(4):
	a += w
	sum += a
print sum
