d = [0 for i in xrange(1001)]
for i in xrange(1,1000):
    for j in xrange(i,1000):
        w = int((i * i + j * j) ** 0.5)
	if i * i + j * j == w * w:
	     if i + j + w <= 1000:
		 d[i+j+w] += 1
key = 0
ans = 0
for i in xrange(1,1001):
    if d[i] > key:
	key = d[i]
	ans = i
print ans
	
