import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	n = int(input())
	coins = list(map(int,input().split()))
	goal = int(input())

	dp = [[0] * (goal + 1) for _ in range(n)]
	dp[0][0] = 1
	for i in range(n):
		for j in range(goal + 1):
			if i > 0:
				dp[i][j] += dp[i - 1][j]
			if j >= coins[i]:
				dp[i][j] += dp[i][j - coins[i]]
	print(dp[n - 1][goal])
