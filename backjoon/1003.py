import sys
input = sys.stdin.readline

n= int(input())

dp_0 = [0] * 41
dp_1 = [0] * 41

dp_0[0] = 1
dp_1[1] = 1
dp_0[2] = 1
dp_1[2] = 1

for i in range(3, 41):
	dp_0[i] = dp_0[i - 2] + dp_0[i - 1]
	dp_1[i] = dp_1[i - 2] + dp_1[i - 1]

for i in range(n):
	num = int(input())
	print(f"{dp_0[num]} {dp_1[num]}")
