limit =  10 ** 5
def Count(d,s):
    for i in s:
	w = ord(i)-ord('0')
	if w == 0:
	    return False
	d[w]+= 1
	if d[w] > 1:
	    return False
    return True
ans = 0
for i in xrange(2,limit):
    for j in xrange(2,int(i ** 0.5)+1):
	if i % j == 0:
	   flag = True
	   d = [0 for t in xrange(10)]
	   w = i / j
	   if Count(d,str(w)) == False:
	       continue
	   if Count(d,str(i)) == False:
	       continue
	   if Count(d,str(j)) == False:
	       continue
	   for k in xrange(1,10):
	       if d[k] != 1:
		   flag = False
	   if flag == True:
	       print i
	       ans += i
	       break
print ans
