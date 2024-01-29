import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
	s, e = list(map(int,input().split()))
	arr.append((e, s))
arr.sort()
ans = 0
time = 0
for i in arr:
	e, s = i
	if time > s:
		continue
	# print(f'time{time} - start{s} / end{e} ')
	ans += 1
	time = e
print(ans)
