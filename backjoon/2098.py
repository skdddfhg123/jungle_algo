import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0] * (n + 1) for _ in range(n + 1)]
check = [0] * n

ans = [16 * 1000000] * (n )
def sol(d, total, start):
	global ans
	if d == n:
		ans[start] = min(ans[start], total)
	for i in range(n):
		if check[i] == 0 and arr[d][i] and total + arr[d][i] <= ans[start]:
			check[i] = 1
			sol(d + 1, total + arr[d][i], start)
			check[i] = 0

for i in range(n):
	sol(0, 0, i)

# print(arr)
print(min(ans))
