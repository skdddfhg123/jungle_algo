import sys
input = sys.stdin.readline

for _ in range(int(input())):
	data = input()
	ans = 0
	add = 0
	for i in range(len(data)):
		if data[i] == 'O':
			add += 1
		else:
			add = 0
		ans += add
	print(ans)