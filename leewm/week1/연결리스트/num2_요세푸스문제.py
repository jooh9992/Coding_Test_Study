from collections import deque

N, K = map(int, input().split())

queue=deque([i for i in range(1,N+1)]) # N까지 오름차순 배열 생성

print('<', end='')
while(len(queue)!=1): # queue에 남은 값이 2개 이상일때 계속 실행
    queue.rotate(-(K-1)) # K-1번째까지 회전시켜서 뒤로 보내기
    print(queue.popleft(), end=', ') # K번째 수 삭제

print(queue.popleft(),end='')
print('>')
