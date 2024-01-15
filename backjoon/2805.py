# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))

# arr.sort(reverse=True)

# n_idx = 0
# for i in range(len(arr)):
# 	if arr[n_idx] != arr[i]:
# 		n_idx = i
# 		break

# #추가되는 나무 수
# add = n_idx

# #자를 높이
# cut = arr[0] - 1
# #반복문 종료 조건 M보다 커질 때
# cmp = 0

# while cmp + add < m:
# 	if n_idx < len(arr) - 1 and cut == arr[n_idx]:
# 		n_idx += 1
# 		add += 1
# 	cmp = cmp + add
# 	# print(f'cmp:{cmp}/cut:{cut}/n_idx:{n_idx}/add:{add}')
# 	cut -= 1

# print(cut)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

def check(cut):
    total = 0
    for height in arr:
        if height <= cut:
            break
        total += height - cut
    return total

left, right = 0, arr[0]
answer = 0

while left <= right:
    mid = (left + right) // 2
    total = check(mid)

    if total < m:
        right = mid - 1
    else:
        answer = mid
        left = mid + 1

print(answer)

