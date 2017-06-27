import sys


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("""Usage: 
			python basic.py [your name]""")
		exit(-1)

	print("Hello {} from {}".format(sys.argv[1], sys.argv[0]))