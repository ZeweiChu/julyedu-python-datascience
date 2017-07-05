# import code
# if __name__ == "__main__":

# 	stocks = {}
# 	with open("nasdaqlisted.txt", "r") as f:
# 		for line in f:
# 			# code.interact(local=locals())
# 			# print(line)
# 			line = line.split("|")
# 			stocks[line[0]] = line[1]

# 	code.interact(local=locals())


# 	# stocks["AAPL"]


# concatenate all .md files to be a single file

import os
basedir = "/Users/zeweichu/julyedu/python-data-science/Basics/"
files = ['1-unix-git.md', '2-intro.md', '2-intro.ppt', '3-Python-basics.md', '4-type-variable-operation-expression.md', '5-list.md', '6-string.md', 'basic.py', "NOTAFILE.md"]
content = ""
for fname in files:
	if fname.endswith(".md"):
		file = basedir + fname
		try:
			with open(file, "r") as f:
				for line in f:
					content += line
		except IOError:
			print("file {} does not exist".format(fname))


with open("out.md", "w") as f:
	f.write(content)


	