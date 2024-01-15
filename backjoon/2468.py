import sys
from collections import deque, namedtuple

Pair = namedtuple('Pair', ['X', 'Y'])

input = sys.stdin.readline

dx = [0, 1, 0 ,-1]
dy = [1, 0, -1, 0]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
h_area = max(max(row) for row in arr)

ans = 0
q = deque()

def sol(n):
	global arr
	global q
	global ans
	cnt = 0
	vis = [[False] * N for _ in range(N)]
	for i in range(N):
		for j in range(N):
			if vis[i][j] == False and arr[i][j] >= n:
				vis[i][j] = True
				cnt += 1
				q.append(Pair(i, j))
				while q:
					cur = q.popleft()
					for dir in range(4):
						nx = cur.X + dx[dir]
						ny = cur.Y + dy[dir]
						if not (0 <= nx < N and 0 <= ny < N):
							continue
						if arr[nx][ny] >= n and vis[nx][ny] == False:
							q.append(Pair(nx, ny))
							vis[nx][ny] = True
	ans = max(ans, cnt)

for n in range(1, h_area + 1):
	sol(n)

print(ans)
