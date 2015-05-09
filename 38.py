ans = 0
for i in xrange(2,10):
    for j in xrange(1,int(10 ** ((9/i)+1))):
	a = ""
	for k in xrange(1,i+1):
	    a += str(k*j)
	l = list(a)
	l.sort()
	if len(l) == 9:
	   flag = True
	   for k in xrange(1,10):
	       if k != ord(l[k-1])-ord('0'):
		   flag = False
	           break
   	   if flag == True:
	       if int(a) > ans:
	           ans = int(a) 
print ans
