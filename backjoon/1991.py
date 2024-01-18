import sys
input = sys.stdin.readline

node = []

for _ in range(int(input())):
	p, c1 ,c2 = list(input().split())
	node.append([p, c1, c2])

ans = []

def find_node(target):
	global node
	for i in range(len(node)):
		if node[i][0] == target:
			return i
	return -1


def add_node(index, type):
	global ans
	if index == -1:
		return
	parent = node[index][0]
	if node[index][1] != '.':
		left = node[index][1]
	else:
		left = -1
	if node[index][2] != '.':
		right = node[index][2]
	else:
		right = -1
	if type == 0:
		ans.append(parent)
		add_node(find_node(left), 0)
		add_node(find_node(right), 0)
	elif type == 1:
		add_node(find_node(left), 1)
		ans.append(parent)
		add_node(find_node(right), 1)
	elif type == 2:
		add_node(find_node(left), 2)
		add_node(find_node(right), 2)
		ans.append(parent)

add_node(0, 0)
print(''.join(ans))
ans = []
add_node(0, 1)
print(''.join(ans))
ans = []
add_node(0, 2)
print(''.join(ans))
