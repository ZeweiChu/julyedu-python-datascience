def gcd(p, q):
	if q == 0:
		return p
	else:
		return gcd(q, p % q)


def fibonacci(n):
	if (n == 0 or n == 1):
		return n;
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a+b
	return a