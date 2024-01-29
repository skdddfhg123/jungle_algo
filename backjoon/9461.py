import sys
input = sys.stdin.readline

dp = [0] * 103
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 3
dp[6] = 4
for i in range(7, 103):
	dp[i] = dp[i - 1] + dp[i - 5]


for _ in range(int(input())):
	n = int(input())
	print(dp[n - 1])