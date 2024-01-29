import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1000005
pre_dp = [0] * 1000005

dp[1] = 0
for i in range(2, n + 1):
	dp[i] = dp[i - 1] + 1
	pre_dp[i] = i - 1
	if i % 2 == 0 and dp[i] > dp[i//2] + 1:
		print(i)
		dp[i] = dp[i//2] + 1
		pre_dp[i] = i//2
	if i % 3 == 0 and dp[i] > dp[i//3] + 1:
		dp[i] = dp[i//3] + 1
		pre_dp[i] = i//3

print(dp[:n+ 2])
print(pre_dp[:n+ 2])