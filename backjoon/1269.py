import sys, heapq
input = sys.stdin.readline

arr = list(map(int, input().split()))
arr_a = set(map(int, input().split()))
arr_b = list(map(int, input().split()))

# arr_a = set(arr_a)
same_cnt = 0
for i in range(len(arr_b)):
    if arr_b[i] in arr_a:
        same_cnt += 1

print(len(arr_a) + len(arr_b) - same_cnt * 2)
