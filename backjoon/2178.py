import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
board = [list(map(int,input().strip())) for _ in range(N)]

q = deque()

q.append([0, 0])
while q:
	y , x = q.popleft()
	for dir in range(4):
		nx = x + dx[dir]
		ny = y + dy[dir]
		if nx < 0 or ny < 0 or nx >= M or ny >= N:
			continue
		if board[ny][nx] == 1:
			board[ny][nx] = board[y][x] + 1
			q.append([ny, nx])

print(board[N - 1][M - 1])
