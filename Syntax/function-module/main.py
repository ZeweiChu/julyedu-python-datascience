import utils
if __name__ == "__main__":
	stocks = utils.load_stocks("nasdaqlisted.txt")
	while 1:
		stock_code = input('Enter a stock code:')
		if stock_code == "exit":
			exit(-1)
		print(utils.get_company_name_by_stock_code(stock_code, stocks))
