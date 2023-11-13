from collections import deque

N=int(input("N: "))
queue=deque([i for i in range(N,0,-1)]) 

while(1):
    queue.pop() # 맨 위에 수 제거
    queue.rotate() # 맨 위에 수 맨 앞으로 보내기

    if len(queue)==1: # 마지막에 남는 수 출력
        print(queue.pop())
        break


### 구현 내용 설명 ###

# 1. line 4에서 
'''
1번 카드가 제일 위에 오도록 정렬
'''

# 2. line 6~12에서
'''
line 7에서 맨 위에 수 제거
line 8에서 맨 위에 수 맨 앞으로 보내기
line 10~12에서 마지막에 남는 수 출력
'''