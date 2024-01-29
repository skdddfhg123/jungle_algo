import sys
input = sys.stdin.readline

dp = [0] * 1002
dp[1] = 1
dp[2] = 2
n = int(input())

for k in range(3, n + 1):
	dp[k] = (dp[k - 2] + dp[k - 1]) % 10007

print(dp[n])
