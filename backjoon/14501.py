import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data = [0] + data
for i in range(1, n + 1):
	data[i][0] += i
print(data)
dp = [[0] * (n + 2) for _ in range(n + 1)]

for i in range(1, n + 1):
	for j in range(1, n + 2):
		if j >= data[i][0]:
			dp[i][j] = max(dp[i-1][j], dp[i-1][j - data[i][0]] + data[i][1])
		else:
			dp[i][j] = dp[i-1][j]
print(dp)
