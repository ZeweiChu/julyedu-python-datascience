import csv
import code

in_file = open("sample.csv", "r")
csv_reader = csv.reader(in_file)
data = list(csv_reader)
print(data)
in_file.close()

in_file = open("sample.csv", "r")
csv_reader = csv.reader(in_file)
for line in csv_reader:
	print("line #: {}, content: {}".format(csv_reader.line_num, line))
in_file.close()

out_file = open("output.csv", "w")
out_writer = csv.writer(out_file)
out_writer.writerow(["julyedu", "baidu", "tencent", "alibaba"])
out_writer.writerow(["fb", "goog", "aapl", "amzn"])
out_writer.writerow([1, -2, 3.1111, 4.5])
out_file.close()

out_file = open("output.tsv", "w")
out_writer = csv.writer(out_file, delimiter="\t")
out_writer.writerow(["julyedu", "baidu", "tencent", "alibaba"])
out_writer.writerow(["fb", "goog", "aapl", "amzn"])
out_writer.writerow([1, -2, 3.1111, 4.5])
out_file.close()
