import sys
input = sys.stdin.readline

N, S = list(map(int, input().split()))

arr = list(map(int, input().split()))

ans = 0
def sol(n, total):
	global N
	global S
	global ans
	# print(f'{n} total:{total}')
	if n == N:
		# print("!!!!")
		if total == S:
			ans += 1
		return
	sol(n + 1, total + arr[n])
	sol(n + 1, total)

sol(0, 0)
if S == 0:
	ans -= 1

print(ans)
