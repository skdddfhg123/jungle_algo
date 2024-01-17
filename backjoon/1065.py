import sys
input = sys.stdin.readline

n = int(input())

if n < 100:
	print(n)
else:
	cnt = 99
	for i in range(100, n + 1):
		h = i // 100
		t = (i // 10) % 10
		o = i % 10

		if h - t == t - o:
			cnt += 1
	print(cnt)
