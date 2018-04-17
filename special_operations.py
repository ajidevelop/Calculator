def log (b, c):
	n = 0
	while (c >= 1):
		c = c / b
		n = n + 1
		if (c <= 1):
			print(n)
			break

