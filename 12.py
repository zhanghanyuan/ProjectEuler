for i in range(1,1000000):
    cnt = 0; w = i * (i+1) / 2
    for j in range(1,int(w ** 0.5)+1):
	if w % j == 0:
	   cnt += 1
	   if j * j != w:
	       cnt += 1
    if w < 100:
        print (w,cnt)
    if cnt >= 500:
	print w
	break
