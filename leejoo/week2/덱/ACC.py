import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    arr = deque(input().strip()[1:-1].split(","))

    #R이 들어올 때마다 reverse를 하면 시간초과가 발생한다.
    #flag를 사용해서 뒤집기를 몇번하는지 구한다.
    flag = 0

    #배열을 [] 입력받으면 공백이 포함되기 때문에 0이면 공백없는 배열을 만들어줌
    if n == 0:
        arr = []

    for i in p:
        if i == 'R':
            flag += 1
        #버리기할 때 배열이 비어있으면 error를 출력
        #배열에 값이 있다면 flag의 개수를 비교해서 앞 or 뒤 값을 제거
        elif i == 'D':
            if len(arr) == 0:
                print('error')
                break
            else:
                if flag % 2 == 1:
                    arr.pop()
                else:
                    arr.popleft()
    
    else:
        if flag % 2 == 1:
            arr.reverse()
        print('[' + ','.join(arr) +']')
    