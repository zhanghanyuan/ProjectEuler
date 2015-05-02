f = open("1.in","r")
a = []
for line in f.readlines():
    s = map(int,line.split())
    a.append(s)
i = 1
l = len(a)
while i < l:
    for j in range(i+1):
	tmp = a[i][j]
	if j < i:
	    a[i][j] = max(a[i][j],tmp+a[i-1][j])
	if j > 0:
	    a[i][j] = max(a[i][j],tmp+a[i-1][j-1]) 
    i += 1
ans = 0
for j in range(l):
    ans = max(ans,a[l-1][j])
print ans
