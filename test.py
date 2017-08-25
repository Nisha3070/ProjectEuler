def score(x,y):
	i = 0
	score = 0

	while i < len(x):
		score += ord(x[i]) - 64
		i += 1
	return y*score 

print score("COLIN",938)