a = [1,2,5,10,20,50,100,200]
f = [0 for i in xrange(201)]
f[0] = 1
for i in a:
    for j in xrange(201):
	if j+i <= 200:
	   f[j+i] += f[j]
print f[200]
	
