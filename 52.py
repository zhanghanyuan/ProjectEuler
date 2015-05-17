def judge(a,b):
    b.sort()
    w = len(b)
    for i in xrange(w):
	if a[i] != b[i]:
	    return False
    return True
g = 10
while True:
    w = g * 6
    if len(str(g)) == len(str(w)):
	a = list(str(g))
	a.sort()
	flag = True
	for i in xrange(2,7):
	    if not judge(a,list(str(i*g))):
		flag = False
		break
	if flag:
	    print g
	    break
    g += 1
