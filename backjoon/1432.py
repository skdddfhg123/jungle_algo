import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().strip())) for _ in range(n)]
graph = [[] for _ in range(n + 1)]
check = [0] * (n + 1)

for y in range(n):
	for x in range(n):
		if arr[y][x] == 1:
			graph[y + 1].append(x + 1)
			check[x + 1] += 1

ans = []
q = deque()
for i in range(1, n + 1):
	if check[i] == 0:
		q.append(i)
		ans.append(i)
		# print(i)
# print(f"check\n{check}\ngraph\n{graph}")

while q:
	cur = q.popleft()
	# ans.append(cur)
	for next in graph[cur]:
		if next not in ans:
			ans.append(next)
		check[next] -= 1
		# if check[next] == 0:
		q.append(next)
if ans:
	print(" ".join(map(str, ans)))
else:
	print("-1")
