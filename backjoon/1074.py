import sys
input = sys.stdin.readline

n, r, c = list(map(int, input().split()))

def sol(N, y, x, t):
	# print(t)
	if N == 0:
		print(t)
		return
	n = pow(2, N - 1)
	# print(n)
	#4사분면
	if x >= n and y >= n:
		sol(N - 1, y - n, x - n, t + pow(n, 2) * 3)
		# print(pow(n, 2) * 3)
	#3사분면
	elif x < n and y >= n:
		sol(N - 1, y - n, x, t + pow(n, 2) * 2)
		# print(pow(n, 2) * 2)
	#2사분면
	elif x >= n and y < n:
		sol(N - 1, y, x - n, t + pow(n, 2) * 1)
	#1사분면
	else:
		sol(N - 1, y, x, t)
# print(f"n{n} r{r} c{c}")
ret = sol(n,r,c,0)
# print(ret)