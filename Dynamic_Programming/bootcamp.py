def fibonacci(n, cache={}):
	if n<=1:
		return n
	elif n not in cache:
		return fibonacci(n-1,cache)+fibonacci(n-2, cache)
	return cache[n]

print fibonacci(5)


def fibonacci_2(n):

	if n<=1:
		return n

	f_minus_2, f_minus_1= 0,1

	for i in range(1,n):
		f = f_minus_2+ f_minus_1
		f_minus_2, f_minus_1= f_minus_1, f

	return f_minus_1

print fibonacci_2(5)

