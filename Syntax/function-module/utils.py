

def load_stocks(filename):

	stocks = {}
	with open(filename, "r") as f:
		for line in f:
			line = line.split("|")
			stocks[line[0]] = line[1]

	return stocks

def get_company_name_by_stock_code(stock_code, stocks):
	stock_code = stock_code.upper()
	if stock_code in stocks:
		return stocks[stock_code]
	else:
		return "Stock code does not exist"
