import sys
input = sys.stdin.readline

V, E = list(map(int, input().split()))
roots = [i for i in range(V + 1)]
nodes = [list(map(int, input().split())) for _ in range(E)]
# print(nodes)
nodes.sort(key=lambda x: x[2])
def find(x):
	if x != roots[x]:
		roots[x] = find(roots[x])
	return roots[x]

ans = 0
for s, e, w in nodes:
	s_root = find(s)
	e_root = find(e)
	if s_root != e_root:
		if s_root > e_root:
			roots[s_root] = e_root
		else:
			roots[e_root] = s_root
		ans += w

print(ans)