n = int(input())
data = list(map(int, input().split()))

ans = 0

for i in range(n):
	flag = False
	m = data[i]
	if m == 1:
		continue
	for j in range(2, m):
		if m % j == 0:
			flag = True
	if not flag:
		ans += 1
	else:
		flag = False

print(ans)