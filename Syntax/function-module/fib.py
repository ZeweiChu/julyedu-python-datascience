import code
def fib(n):
	a, b = 0, 1
	for i in range(n):
		print(a, end=" ")
		a, b = b, a+b
	print()

# fib(5)
# fib(10)
# fib(30)
# fib(100)


def print_all(*args):
	print(type(args))
	print(args)

# print_all("hello", "world", "julyter", "notebook")

def unpack_args(a, b):
	print(a, b)

r = [2,5]
r = 2,5
# unpack_args(r)
unpack_args(*r)

