
def load_stocks(filename):
	stocks = {}
	with open(filename, "r") as f:
		i = 0
		for line in f:
			if i == 0:
				headers = line.strip().split("|")
			else:
				elements = line.strip().split("|")
				stock_info = {}
				for j in range(1, len(headers)):
					stock_info[headers[j]] = elements[j]
				stocks[elements[0]] = stock_info
			i += 1
	return stocks
