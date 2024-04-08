import sys
import heapq

input = sys.stdin.readline

# 입력 받기
arr = list(map(int, input().split()))
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

# arr_b를 힙으로 변환
heapq.heapify(arr_b)

# arr_b의 요소 중 arr_a에 없는 것들을 arr_a에 추가
while arr_b:
    arr_a.append(heapq.heappop(arr_b))

# 정렬된 리스트 생성
arr_a.sort()

# 출력
print(*arr_a)