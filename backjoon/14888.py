import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
cal = list(map(int, input().split()))
def sol(d, n):
	global min_ans
	global max_ans
	if d == N - 1:
		if n < min_ans:
			min_ans = n
		if n > max_ans:
			max_ans = n
		return
	for i in range(4):
		if cal[i] and i == 0:
			cal[i] -= 1
			sol(d + 1, n + nums[d + 1])
			cal[i] += 1
		elif cal[i] and i == 1:
			cal[i] -= 1
			sol(d + 1, n - nums[d + 1])
			cal[i] += 1
		elif cal[i] and i == 2:
			cal[i] -= 1
			sol(d + 1, n * nums[d + 1])
			cal[i] += 1
		elif cal[i] and i == 3:
			cal[i] -= 1
			if n < 0:
				tmp = abs(n) // nums[d + 1]
				tmp *= -1
			else:
				tmp = n // nums[d + 1]
			sol(d + 1, tmp)
			cal[i] += 1

min_ans = 10000000000
max_ans = -10000000000

sol(0, nums[0])
print(max_ans)
print(min_ans)