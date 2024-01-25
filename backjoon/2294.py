import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))

arr = []
for _ in range(n):
	arr.append(int(input()))
arr.sort()

dp = [10001] * (k + 1)
dp[0] = 0

for num in arr:
	for i in range(num, k + 1):
		dp[i] = min(dp[i], dp[i - num] + 1)

if dp[k] == 10001:
	print("-1")
else:
	print(dp[k])
