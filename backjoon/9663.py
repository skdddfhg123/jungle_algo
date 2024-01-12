N = int(input())

ans = 0

y_check = [False] * 15
xpy_check = [False] * (15 * 15)
xmy_check = [False] * (15 * 15)

def sol(y):
	global ans
	if y == N:
		ans += 1
	for x in range(N):
		if not y_check[x] and not xpy_check[x + y] and not xmy_check[x - y]:
			y_check[x] = True
			xpy_check[x + y] = True
			xmy_check[x - y] = True
			sol(y + 1)
			y_check[x] = False
			xpy_check[x + y] = False
			xmy_check[x - y] = False

sol(0)
print(ans)
