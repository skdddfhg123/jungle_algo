import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))
data = [0] + data
dp = [0] * (n + 1)
max_dp = [0] * (n + 1)

len = 0
for i in range(1, n + 1):
	for j in range(1, n + 1):
		if max_dp[j] == 0 or max_dp[j] == data[i]:
			max_dp[j] = data[i]
			dp[i] = j
			break
		elif max_dp[j] > data[i]:
			max_dp[j] = data[i]
			dp[i] = j
			break

print(max(dp))
