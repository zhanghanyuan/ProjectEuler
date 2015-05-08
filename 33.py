ans1 = 1;ans2 = 1
def gcd(x,y):
    if y == 0:
	return x
    else:
	return gcd(y,x%y)
for i in xrange(10,100):
    for j in xrange(i+1,100):
            a = i % 10
	    b = i / 10
	    c = j % 10
	    d = j / 10
	    if a == c and b * j == i * d and c != 0:
	        ans1 *= b; ans2 *= d
	    	continue
	    if a == d and b * j == i * c:
		ans1 *= b; ans2 *= c
		break
	    if b == c and a * j == i * d:
		ans1 *= a; ans2 *= d
		break
	    if b == d and a * j == i * c:
		ans1 *= a; ans2 *= c
		break 	
ans2 /= gcd(ans1,ans2)
print ans2
	
