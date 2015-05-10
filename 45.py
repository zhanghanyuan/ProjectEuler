def isDigit(a,b,c):
    w = int((b ** 2 - 4 * a * c) ** 0.5)
    if w * w == (b ** 2 - 4 * a * c):
	if (-b+w) % (2*a) == 0:
	    return True
    return False
i = 286
while True:
    t = i * (i+1) / 2
    if isDigit(3,-1,-2*t) == True and isDigit(2,-1,-t) == True:
	print t
	break
    i += 1
