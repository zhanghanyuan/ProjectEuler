def ami(x):
    cnt = 1
    for i in range(2,int(x ** 0.5)+1):
	if x % i == 0:
	    cnt += i
	    if i * i != x:
		cnt += x / i
    return cnt
sum = 0
for i in range(2,10001):
    j = ami(i)
    if i != j and ami(j) == i:
	print (i,j)
	sum += i
print sum	
