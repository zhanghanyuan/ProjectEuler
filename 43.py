import itertools
d = [2,3,5,7,11,13,17]
ans = 0
for i in itertools.permutations("0123456789",10):
    flag = True
    for j in xrange(1,8):
	w = (ord(i[j])-ord('0'))*100+(ord(i[j+1])-ord('0'))*10+ord(i[j+2])-ord('0')
	if w % d[j-1] !=0 :
	    flag = False
	    break 
    if flag == True:
	t = 0
	for j in i:
	    t = t * 10 + ord(j)-ord('0')
	ans += t 
print ans
