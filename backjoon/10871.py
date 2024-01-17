import sys
input = sys.stdin.readline

N, X = map(int, input().split())
data = list(map(int, input().split()))

ans = []
for a in data:
	if a < X:
		ans.append(a)
print(*ans)
