import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
	r, g, b = list(map(int, input().split()))
	data.append([r, g, b])
dp = [[0, 0, 0] for _ in range(n + 1)]
dp[0][0] = data[0][0]
dp[0][1] = data[0][1]
dp[0][2] = data[0][2]
for i in range(1, n):
	dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + data[i][0]
	dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + data[i][1]
	dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + data[i][2]

print(min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))
