limit = 28123
a = [0 for i in range(limit+1)]
for i in range(1,limit+1):
    sum = 1
    for j in range(2,int(i ** 0.5)+1):
	if i % j == 0:
	    sum += j
	    if j * j != i:
	        sum += i / j 
    if sum > i:
	a[i] = 1
ans = 0
for i in range(1,limit+1):
    flag = False
    for j in range(1,i):
	if a[j] == 1 and a[i-j] == 1:
	    flag = True
	    break 
    if flag == False:
	ans += i
print ans
