import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("""Usage: 
			python basic.py [a number]""")
		exit(-1)

	a = float(sys.argv[1])
	if a < 0:
		print("negative")
	elif a == 0:
		print("zero")
	else:
		print("positive")