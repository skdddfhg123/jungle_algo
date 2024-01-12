idx = -1
max = 0

for i in range(9):
	cmp = int(input())
	if cmp > max:
		max = cmp
		idx = i + 1

print(f"{max}\n{idx}")