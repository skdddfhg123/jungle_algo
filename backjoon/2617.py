import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

graph = [[[], []] for _ in range(N + 1)]

for _ in range(M):
	large, small = list(map(int, input().split()))
	graph[small][0].append(large)
	graph[large][1].append(small)

def check(n, flag, arr):
	vis.add(n)
	for i in range(len(graph[n][flag])):
		if graph[n][flag][i] not in vis:
			arr.append(graph[n][flag][i])
			check(graph[n][flag][i], flag, arr)

ans = [False] * (N + 1)
for i in range(1, N + 1):
	if graph[i][0]:
		vis = set()
		arr = []
		check(i, 0, arr)
		# print(arr)
		if len(arr) > N // 2:
			ans[i] = True
	if graph[i][1]:
		vis = set()
		arr = []
		check(i, 1, arr)
		# print(arr)
		if len(arr) > N // 2:
			ans[i] = True

ret = 0
for i in range(1, N + 1):
	if ans[i] == True:
		ret += 1


print(ret)
