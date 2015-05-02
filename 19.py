import datetime
ans = 0
for i in range(1901,2001):
    for j in range(1,13):
        d1 = datetime.datetime(1900,12,31)
        d2 = datetime.datetime(i,j,1)
	if (d2-d1).days % 7 == 6:
	    ans += 1
print ans
