data = []

for _ in range(int(input())):
	data.append(int(input()))

n = len(data)

for i in range(n - 1):
	for j in range(n - 1 - i):
		if data[j] > data[j + 1]:
			data[j], data[j + 1] = data[j + 1], data[j]

for i in range(n):
	print(data[i])