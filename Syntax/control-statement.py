import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("""Usage:
			python control-statement.py [give me a number]""")
		exit(-1)
	else:
		number = float(sys.argv[1])
		if number < 0:
			print("negative number")
		elif number == 0:
			print("zero")
		else:
			print("positive number")

