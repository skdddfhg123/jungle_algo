N, K = map(int, input().split())

arr = list(range(1, N + 1))
ans = []
index = 0

while arr:
    index = (index + K - 1) % len(arr)
    ans.append(arr.pop(index))

print("<" + ", ".join(map(str, ans)) + ">")

# from collections import deque

# def sol(N, K):
#     circle = deque(range(1, N + 1))
#     ans = []

#     while circle:
#         circle.rotate(-(K - 1))
#         ans.append(circle.popleft())

#     return ans

# N, K = map(int, input().split())

# ans = sol(N, K)

# print("<" + ", ".join(map(str, ans)) + ">")