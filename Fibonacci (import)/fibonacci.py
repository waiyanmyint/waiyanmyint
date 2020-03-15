#Fibonacci
Fibonacci.py

# Fibonacci numbers module

#n = int(input('Please enter a number: '))

def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

# Go to fibonacci Powerpoint

def fib2(n): # return Fibonacci series
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result


	#>>> fib #import
