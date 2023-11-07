import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) #카드 개수 입력
queue = deque([i for i in range(1, N+1)]) #카드 수만큼 큐 생성

#카드의 개수가 1장 남을 때까지 반복
#첫장을 popleft로 버리고 그 다음장을 마지막에 append해줌
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])