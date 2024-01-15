import sys
input = sys.stdin.readline
M, N, L = list(map(int, input().split()))
positions = list(map(int, input().split()))
positions.sort()
def b_search(data, key):
	l, r = 0, len(data) - 1
	while l <= r:
		m = (l + r) // 2
		if data[m] == key:
			return m
		elif data[m] < key:
			l = m + 1
		else:
			r = m - 1
	return r
ans = 0
for _ in range(N):
	x, y = list(map(int, input().split()))
	i = b_search(positions, x)
	if i < M - 1 and abs(x - positions[i + 1]) + y <= L:
		ans += 1
	elif abs(x - positions[i]) + y <= L:
		ans += 1
print(ans)