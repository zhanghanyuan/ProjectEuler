f = open("words.txt","r")
words = f.read().split(",")
ans = 0
for i in words:
    j = i.strip('"')
    w = 0
    for k in j:
	w += ord(k)-ord('A')+1
    g = int((1+8*w) ** 0.5)
    if g * g == 1 + 8 * w:
	ans += 1 
print ans
