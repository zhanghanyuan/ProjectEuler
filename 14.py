limit = 1000000
vis = [0 for i in range(1,limit+22)]
for i in range(2,limit+1):
    if vis[i] != 0:
	continue
    w = i
    cnt = 0
    while w != 1:
	if w <= limit and vis[w] != 0:
	    cnt += vis[w]
	    break 
	cnt += 1
	if w % 2 == 0:
	    w = w/2
	else:
	    w = 3*w+1	
    vis[i] = cnt
ans = 0
t = 0
for i in range(2,limit+1):
    if ans < vis[i]:
        ans = max(ans,vis[i])
	t = i
print t 
