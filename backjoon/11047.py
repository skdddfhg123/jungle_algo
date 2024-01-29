import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
arr = []

for i in range(n):
	arr.append(int(input()))

ans = 0
for i in range(n-1, -1, -1):
	ans += k // arr[i]
	print(f"arr[i]{arr[i]}\nans = {ans}")
	k %= arr[i]

print(ans)
