import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
data = list(map(int, input().split()))

add_arr = []
sub_arr = []
add_arr.append(data[0])
sub_arr.append(0)
sum = data[0]
sub = 0
for i in range(1, n):
	sum += data[i]
	sub += data[i - 1]
	add_arr.append(sum)
	sub_arr.append(sub)

for i in range(m):
	s, e = list(map(int,input().split()))
	print(add_arr[e - 1] -  sub_arr[s - 1])
