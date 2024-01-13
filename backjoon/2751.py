import sys
data = []
for _ in range(int(sys.stdin.readline())):
	data.append(int(sys.stdin.readline()))
# 4424ms
def m_sort(a):
    def merge_sort(a, left, right):
        if left < right:
            center = (left + right)// 2
            merge_sort(a, left, center)
            merge_sort(a, center + 1, right)
            p = j = 0
            i = k = left
            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1
            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1
    n = len(a)
    buff = [None] * n
    merge_sort(a, 0, n - 1)
m_sort(data)
for i in range(len(data)):
    print(data[i])


# # 1152ms
# check = [False] * 2000001

# n = int(sys.stdin.readline())

# for _ in range(n):
#     check[int(sys.stdin.readline()) + 1000000] = True

# for i in range(2000001):
#     if check[i]:
#         print(i - 1000000)
