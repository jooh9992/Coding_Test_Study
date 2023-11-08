import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
queue = deque([i for i in range(1, N+1)])
count = 0 #2,3번 연산의 값을 저장하는 변수

for i in arr: #뽑아내려는 수를 반복
    while True:
        if i == queue[0]: #덱에 있는 처음 값이 뽑으려는 값과 똑같으면 
            queue.popleft() #삭제
            break
        else: #덱에 있는 처음 값이 현재 뽑으려는 수와 같지 않으면 2,3번 연산을 수행
              #2,3번 연산을 하기위해 인덱스 값을 가져와서 앞쪽에 있는지 뒤쪽에 있는지 계산
            if queue.index(i) <= len(queue)//2:
                #rotate를 사용해서 덱 회전을 해줌
                queue.rotate(-1)
                count +=1
            else:
                queue.rotate(1)
                count +=1

print(count)