f = open("1.in","r")
ans = 0
for line in f.readlines():
    w = int(line) 
    ans += w
print ans
