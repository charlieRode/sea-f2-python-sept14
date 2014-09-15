def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
	if n == 0:
		return 0
	elif n == 1:
		return 2
	elif n == 2:
		return 1
	else:
		return lucas(n-1) + lucas(n-2)



def sum_series(n, first = 0, second = 1):
	if n == 0:
		return 0
	elif n == 1:
		return first
	elif n == 2:
		return second
	else: 
		return sum_series(n-1) + sum_series(n-2)

print sum_series(6, 2, 1)



	
