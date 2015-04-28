import heapq

heap = []
heapq.heapify(heap)
file_object = open("1.in")
try:
    all_the_text = file_object.read()
finally:
    file_object.close()
lenth = len(all_the_text)
r = []
for i in range(lenth):
    if all_the_text[i] >= '0' and all_the_text[i] <= '9':
	r.append(ord(all_the_text[i])-ord('0'))
lt = len(r)
i = 0
d = 0
while i < lt:
    if i >= 12:
	j = i
	w = 1
	while j >= i-12:
	    w *= r[j] 
	    j -= 1
        heapq.heappush(heap,-w)	
    i += 1
cnt = 0
ans = 0
pre = 0
while cnt < 1:
    cnt += 1
    ans = -heapq.heappop(heap)
print ans

