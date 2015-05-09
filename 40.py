cnt = 0
i = 0
pre = 0
ans = 1
while cnt <= 10 ** 6:
    i += 1
    s = str(i)
    for j in s:
	w = ord(j)-ord('0')
	cnt += 1
	for k in xrange(7):
	    if cnt == 10 ** k:
		ans *= w	      
print ans	    

