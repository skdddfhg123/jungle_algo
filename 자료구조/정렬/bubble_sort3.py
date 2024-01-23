from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬(스캔 범위를 제한)"""
    n = len(a)
    ccnt = 0  # 비교 횟수
    scnt = 0  # 교환 횟수
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1):
            if a[j + 1] < a[j]:
                a[j + 1], a[j] = a[j], a[j + 1]
                last = j
                ccnt += 1
        scnt += 1
        k = last
    print(f'비교:{ccnt} / 교환:{scnt}')

if __name__ == '__main__':
    print('버블 정렬을 합니다.')
    num = int(input('원솟수를 입력하세요.: '))
    x = [None] * num    # 원솟수 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    bubble_sort(x)      # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')