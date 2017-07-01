import code
if __name__ == "__main__":

	stocks = {}
	with open("nasdaqlisted.txt", "r") as f:
		for line in f:
			# code.interact(local=locals())
			# print(line)
			line = line.split("|")
			stocks[line[0]] = line[1]

	code.interact(local=locals())


	# stocks["AAPL"]

	