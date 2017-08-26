def isAbd(x):
	n = int(x/2) + 1
	i = 2
	sum = 1

	while i < n:
		if x%i == 0:
			sum += i
		i += 1
	return sum > x

print isAbd(12)