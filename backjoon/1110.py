import sys
input = sys.stdin.readline

num = list(input())
if num[1] == '\n':
	num[1] = int(num[0])
	num[0] = 0
else:
	num[0] = int(num[0])
	num[1] = int(num[1])

new_num = 0
ans = 0
cmp = num[0] * 10 + num[1]
while cmp != new_num:
	ans += 1
	tmp = (num[0] + num[1]) % 10
	num[0] = num[1]
	num[1] = tmp
	new_num = num[0] * 10 + num[1]
	# print(f"ans{ans}/ new{new_num} cmp{cmp}")
if ans:
	print(ans)
else:
	print("1")
