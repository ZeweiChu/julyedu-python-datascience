print("while loop:")
fibs = []
i = 0
j = 1
while i < 500:
	fibs.append(i)
	tmp = j
	j = i + j
	i = tmp
print(fibs)


print("for loop:")
fibs = [0, 1]
for i in range(2, 15):
	fibs.append(fibs[-1] + fibs[-2])

print(fibs)