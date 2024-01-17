import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

total = A * B * C
data = str(total)

ans = [0] * 10

for i in range(len(data)):
	ans[ord(data[i]) - 48] += 1

for a in ans:
	print(a)
	