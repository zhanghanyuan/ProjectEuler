def isPrime(n):
    if n <= 1:
	return False
    for i in xrange(2,int(n ** 0.5)+1):
	if n % i == 0:
	    return False
    return True
x = 9
while True:
    flag = False
    if isPrime(x) == False:
 	for i in xrange(1,int(x ** 0.5)+1):
	    if 2*(i ** 2) < x and isPrime(x - 2 * (i ** 2)) == True:
	   	flag = True 
	    	break
    else:
	flag = True
    if flag == False:
	print x
	break
    x += 2

