import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))

dp = [-1000] * n
for i in range(n):
	dp[i] = max(data[i], dp[i - 1] + data[i])

print(max(dp))
