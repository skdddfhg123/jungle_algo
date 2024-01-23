n = input()

def cal(num, cnt):
	if num == "00":
		print(1)
		return None

	if num[1] == "0":
		new_n = str(int(num[0])*2)
	else: 
		new_n = str(int(num[0])+int(num[1]))

	count = cnt

	print("new_n:", new_n)

	if new_n == n:
		count += 1
		print("count:",count)
		return None

	if len(new_n) == 2:
		new_n = num[1]+new_n[1]

	elif num[1] == "0":
		new_n = num[0]+new_n

	else:
		new_n = num[1]+new_n

	count += 1
	cal(new_n, count)


# if int(n) < 10:
# 	m = n+"0"
# 	print("m:", m)
	# cal(m, 0)
# elif int(n) < 100:
	cal(n, 0)

# else:
# 	None