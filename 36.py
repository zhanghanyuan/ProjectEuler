def judge(s):
    l = len(s)
    for i in xrange(l):
	if s[i] != s[l-1-i]:
	    return False
    return True
limit = 10 ** 6
ans = 0
for i in xrange(1,limit):
    if judge(bin(i)[2:]) and judge(str(i)):
	ans += i
print ans
	
