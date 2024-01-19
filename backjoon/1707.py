import sys
sys.stdin.readline
# sys.setrecursionlimit(1000**1)
def dfs(V, arr):
	arr.append(V)
	vis.add(V)
	for i in graph[V]:
		if i not in vis:
			dfs(i, arr)
for _ in range(int(input())):
	N, E = list(map(int,input().split()))
	graph = [[] for _ in range(N + 1)]
	for _ in range(E):
		a, b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)
	vis = set()
	ans = [0] * (N + 1)
	
	flag = False
	for i in range(len(graph)):
		if len(graph[i]) == 2:
			vis.add(i)
			arr1 = []
			dfs(graph[i][0], arr1)
			arr2 = []
			dfs(graph[i][1], arr2)
			intersection = any(element in arr2 for element in arr1)
			if intersection or  graph[i][0] in graph[graph[i][1]]:
				flag = True
				break
			for j in range(1, N + 1):
				if j not in vis:
					flag = True
					break
	if flag:
		print("NO")
	else:
		print("YES")


# for i in range(2, N + 1):
# 	print(ans[i])

