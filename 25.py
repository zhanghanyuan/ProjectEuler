a = 1; b = 1; c = 0; cnt = 0
while True:
    cnt += 1
    if a >= 10 ** (1000-1):
	print cnt
	break
    c = a+b
    a = b
    b = c
