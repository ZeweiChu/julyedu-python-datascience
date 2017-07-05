
# function definition
def hello(n, name="world"):
	print(n)
	print("hello {}".format(name))

# call a hello function
# hello(1)
# # call print function
# print("aaabbb")

def fib(n):
	a, b = 0, 1
	arr = []
	for i in range(n):
		arr.append(a)
		a, b = b, a+b

	return arr

# fibonacci = fib(100)
# print(arr)


def concatenate(*args, sep=" "):
	args = [str(a) for a in args]
	print(sep.join(args))
	# print(type(args))

# concatenate("hello", "world", "jupyter", "notebook", "julyedu", 1, 2, 3, 4, 5, sep="\t")

def print_two_vars(a, b):
	print(a, b)
 
# ab = 2, 5
# print_two_vars( *ab )





