import sys, heapq
input = sys.stdin.readline

# 상,하,좌,우 체크 위한 데이터 미리 선언
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 인풋 데이터
N, K = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
S, Y, X = list(map(int, input().split()))

# heapq는 앞에 데이터가 작은 순으로 정렬 되기에, 시간 순으로 queue를 돌리기 위해 따로 함수를 구현하였음
def sol(hq):
	# 다음 시간에 돌릴 queue데이터를 담기 위한 공간 선언
	ret = []
	while hq:
		node, y, x = heapq.heappop(hq)
		for dir in range(4):
			ny = y + dy[dir]
			nx = x + dx[dir]
			if ny < 0 or ny >= N or nx < 0 or nx >= N:
				continue
			# hq에 담는 것이 아닌, ret에 push를 함으로써 다음 시간에 돌릴 데이터에 추가
			if board[ny][nx] == 0:
				board[ny][nx] = board[y][x]
				heapq.heappush(ret, (node, ny, nx))
	return ret

hq = []
# 바이러스를 퍼트리기 위해 queue에 데이터 넣기
for i in range(N):
	for j in range(N):
		if board[i][j] != 0:
			heapq.heappush(hq, (board[i][j], i ,j))
# 1초부터 S초까지 바이러스 퍼트리기 진행
for time in range(1, S + 1):
	hq = sol(hq)

print(board[Y - 1][X - 1])