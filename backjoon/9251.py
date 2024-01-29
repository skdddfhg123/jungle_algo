import sys
input = sys.stdin.readline

A = list(input().strip())
A = [0] + A
B = list(input().strip())
B = [0] + B
dp = [[0] * (len(B)) for _ in range(len(A))]
# print(A)

for i in range(len(A)):
	for j in range(len(B)):
		if i == 0 or j == 0:
			continue
		if A[i] == B[j]:
			# print(f"i{i} j{j} data{A[i]} data{B[j]}")
			dp[i][j] = dp[i - 1][j - 1] + 1
		else:
			dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# print(dp)
print(dp[len(A) - 1][len(B) - 1])
