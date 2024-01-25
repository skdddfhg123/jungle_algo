import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = list(map(int, input().split()))

board = [list(input().strip()) for _ in range(N)]
vis = [[False] * M for _ in range(N)]

# print(vis)

ans = 0
for i in range(N):
	for j in range(M):
		if not vis[i][j]:
			if board[i][j] == '-':
				vis[i][j] = True
				ans += 1
				cmp = j
				while cmp + 1 < M and board[i][cmp + 1] == '-':
					vis[i][cmp + 1] = True
					cmp += 1
				# print(f"i == i{i} / j{j} / cmp{cmp}")
			elif board[i][j] == '|':
				vis[i][j] = True
				ans += 1
				cmp = i
				while cmp + 1 < N and board[cmp + 1][j] == '|':
					vis[cmp + 1][j] = True
					cmp += 1
				# print(f"j == i{i} / j{j} / cmp{cmp}")

print(ans)
