d = []
limit = 2000000
v = [False for a in range(1,limit+1)]
sum = 0
for i in range(2,limit):
    if v[i] == False:
	sum += i 
	d.append(i) 
    for j in d:
	if j * i >= limit:
	    break
        v[j*i] = True
	if i % j == 0:
	   break
print sum 
