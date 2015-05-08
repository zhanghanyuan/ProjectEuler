import itertools
cnt = 0
for i in itertools.permutations(range(10),10):
    cnt += 1
    if cnt == int(10 ** 6):
	print i
  	break

