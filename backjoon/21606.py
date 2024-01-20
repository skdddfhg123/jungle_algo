import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v, cnt):
	vis.add(v)
	for i in gragh[v]:
		if check[i] == 1:
			cnt += 1
		elif i not in vis and check[i] == 0:
			cnt = dfs(i, cnt)
	return cnt

N = int(input())

ans = 0
check = list(map(int,input().strip()))
check = [-1] + check
gragh = [[] for _ in range(N + 1)]
for _ in range(N - 1):
	a, b = list(map(int, input().split()))
	gragh[a].append(b)
	gragh[b].append(a)
	if check[a] == 1 and check[b] == 1:
		ans += 2
vis = set()
for i in range(1, N + 1):
	if check[i] == 0 and i not in vis:
		x = dfs(i, 0)
		ans += x * (x - 1)

print(ans)