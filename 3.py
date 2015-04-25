a = 600851475143 
ans = 0
for i in range(2,int((a**0.5)+1)): 
    if a % i == 0:
	while a % i == 0:
	    a /= i
	if ans < i:
	    ans = i
if ans < a:
    ans = a
print ans
