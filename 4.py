ans = 0
for i in range(100,1000):
    for j in range(100,1000):
	w = i*j
	s = str(w)
	l = len(s)
	flag = True
	a = 0; b = l-1
	while a < b:
	    if s[a] != s[b]:
		flag = False
		break
	    a += 1; b -= 1
	if flag == True:
	    ans = max(ans,w)
print ans
