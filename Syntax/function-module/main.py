import utils


stocks = utils.load_stocks("function-module/nasdaqlisted.txt")
while True:
	stock_symbol = input("Enter a stock symbol: ")
	if stock_symbol == "exit":
		exit(-1)
	print(stocks[stock_symbol.upper()])
