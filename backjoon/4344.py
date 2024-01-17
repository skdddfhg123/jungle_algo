for _ in range(int(input())):
	data = list(map(int, input().split()))
	average = sum(data[1:]) / data[0]
	cnt = 0
	for i in range(1, len(data)):
		if data[i] > average:
			cnt += 1
	print("{:.3%}".format(cnt/data[0]))
