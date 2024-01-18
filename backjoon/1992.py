import sys
input = sys.stdin.readline

n = int(input())

arr = [list(input()) for _ in range(n)]

ans = []

def compare(n, x, y):
	for i in range(n):
		for j in range(n):
			if arr[i + y][j + x] != arr[y][x]:
				return 0
	return 1

def sol(n, x, y):
	if compare(n, x, y):
		ans.append(arr[y][x])
	else:
		n //= 2
		ans.append('(')
		sol(n, x, y)
		sol(n, x + n, y)
		sol(n, x, y + n)
		sol(n, x + n, y + n)
		ans.append(')')

sol(n, 0, 0)

print("".join(ans))
