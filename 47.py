def isDigit(n):
    if n <= 1:
	return False
    x = n
    cnt = 0
    for i in xrange(2,int(n ** 0.5)+1):
	if x % i == 0:
	    cnt += 1
	    while x % i == 0:
		x /= i	
    if x > 1:
	cnt += 1
    if cnt == 4:
	return True
    else:
	return False
i = 10
while True:
    if isDigit(i) and isDigit(i+1) and isDigit(i+2) and isDigit(i+3):
	print i
	break
    i += 1
