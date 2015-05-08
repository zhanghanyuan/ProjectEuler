limit = 10 ** 6
sum = 0
for i in range(2,limit):
    w = i
    g = 0
    while w > 0:
  	g += (w % 10) ** 5
	w /= 10
    if g == i:
	sum += i
print sum	
