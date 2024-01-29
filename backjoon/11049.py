import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n) for _ in range(n)]
inf = 2 ** 31 - 1

for l in range(1, n):
	for i in range(n - l):
		j = i + l
		dp[i][j] = inf
		for k in range(i, j):
			q = dp[i][k] + dp[k + 1][j] + data[i][0] * data[k][1] * data[j][1]
			if q < dp[i][j]:
				dp[i][j] = q

print(dp[0][n - 1])
