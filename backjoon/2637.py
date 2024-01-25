import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
check = [0] * (n + 1)
arr = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(int(input())):
	a, b, c = list(map(int, input().split()))
	graph[b].append((a, c))
	check[a] += 1

q = deque()
for i in range(1, n + 1):
	if check[i] == 0:
		q.append(i)

while q:
	cur = q.popleft()
	for next, next_need in graph[cur]:
		if arr[cur].count(0) == n + 1:
			arr[next][cur] += next_need
		else:
			for i in range(1, n + 1):
				arr[next][i] += arr[cur][i] * next_need
		check[next] -= 1
		if check[next] == 0:
			q.append(next)

for i in enumerate(arr[n]):
	if i[1] > 0:
		print(*i)
