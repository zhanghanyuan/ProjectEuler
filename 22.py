f = open("names.txt","r")
s = f.read().split(',')
sum = 0
cnt = 0
a = []
for i in s:
    a.append(i.strip('"'))
a.sort()
print a
for i in a:
    cnt += 1
    w = 0
    for j in i:
        w += ord(j)-ord('A')+1	
    sum += w * cnt
print sum
