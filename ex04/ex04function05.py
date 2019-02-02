#	sum = 10 + (1 / k^2) + (1 / (k + 1)^2) + ... + (1 / n^2)

def sqr(n):
	return n * n

def sum_fn(n):
	my_sum = 10.0
	for i in range (1, n + 1):
		my_sum += (1.0 / sqr(i))
	return my_sum