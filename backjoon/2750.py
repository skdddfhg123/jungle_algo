data = []

for _ in range(int(input())):
	data.append(int(input()))

n = len(data)

def q_sort(data, left, right):
	pl = left
	pr = right
	x = data[(left + right) // 2]

	while pl <= pr:
		while data[pl] < x: pl+=1
		while data[pr] > x: pr-=1
		if pl <= pr:
			data[pl], data[pr] = data[pr], data[pl]
			pl+=1
			pr-=1
	
	if left < pr: q_sort(data, left, pr)
	if right > pl: q_sort(data, pl, right)

q_sort(data, 0, len(data) - 1)

for i in range(n):
	print(data[i])