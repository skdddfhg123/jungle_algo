import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

ans = [0, 0]

def sol(x, y, n):
	global board
	cmp = board[x][y]
	flag = False
	for i in range(n):
		for j in range(n):
			if board[x + i][y + j] != cmp:
				flag = True
				break
		if flag:
			break

	if flag == False:
		if cmp == 0:
			ans[0] += 1
		else:
			ans[1] += 1
	else:
		sol(x, y, n//2)
		sol(x+n//2, y, n//2)
		sol(x, y+n//2, n//2)
		sol(x+n//2, y+n//2, n//2)

sol(0, 0, N)

print(ans[0])
print(ans[1])