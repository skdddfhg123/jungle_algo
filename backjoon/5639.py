import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

arr = []
while 1:
	try:
		arr.append(int(input()))
	except:
		break

def sol(s, e):
	if e < s:
		return
	m = e + 1
	for i in range(s + 1, e + 1):
		if arr[i] > arr[s]:
			m = i
			break
	# print(f"s{s}/m{m}/e{e}")
	sol(s + 1, m - 1)
	sol(m, e)
	print(arr[s])

sol(0, len(arr) - 1)
