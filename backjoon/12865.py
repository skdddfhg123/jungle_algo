import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

# print(data)
for i in range(N):
	for j in range(1, K + 1):
		if i > 0:
			if j >= data[i][0]:
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - data[i][0]] + data[i][1])
			else:
				dp[i][j] = dp[i - 1][j]
				
		else:
			if j >= data[i][0]:
				dp[i][j] = data[i][1]

print(dp[N - 1][K])
# print(dp)