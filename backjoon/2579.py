import sys
input = sys.stdin.readline

n = int(input())
data = [] * (304 + 1)

ans = 0
for i in range(n):
	data.append(int(input()))
	ans += data[i]
if n <= 2:
	print(ans)
	exit()

dp = [0] * (304 + 1)
dp[0] = data[0]
dp[1] = data[1]
dp[2] = data[2]
for i in range(3, n):
	dp[i] = data[i] + min(dp[i - 3], dp[i - 2])

print(ans - min(dp[n - 3], dp[n - 2]))
