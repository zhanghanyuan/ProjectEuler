files = open("1.in","r")
result = []
for line in files.readlines():
    result.append(line.split())
lr = len(result); lc = len(result[0])
print (lr," ",lc)
def num(s):	
    sum = 0
    for i in s:
	sum = sum*10+ord(i)-ord('0')	
    return sum
def dir(x,y,dx,dy):
    i = x; j = y; cnt = 0
    t = 1
    while cnt < 4:
	if i >= lr or j >= lc or i < 0 or j < 0:
	   t = 0; break	
        t *= num(result[i][j])
	i += dx; j += dy
    	cnt += 1
    return t	
i = 0; j = 0
ans = 0
while i < lr and j < lc:
    ans = max(ans,dir(i,j,1,0))
    ans = max(ans,dir(i,j,0,1))
    ans = max(ans,dir(i,j,1,1))
    ans = max(ans,dir(i,j,1,-1))
    if j+1 == lc:
	i += 1; j = 0
    else:
	j += 1
print ans 
     
