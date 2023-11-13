from collections import deque

T = int(input())
p = input()
print(p)

print(p.split('rd'))
from collections import deque

T = int(input())
error=0

for i in range(T):
    p=list(map(str, input()))
    n=int(input())

    li=input().replace("[", "").replace("]", "")
    if len(li)!=0:
        li= deque(map(int,li.split(',')))
    else:
        li=deque(li)

    count_R=0
    for j in range(len(p)):
        if p[j]=='R':
            count_R+=1
        else:
            if len(li)==0:
                print('error')
                error=1
                break
            else:
                if count_R % 2 ==0:
                    li.popleft()
                else:
                    li.pop()

    if error == 1:
        continue
    else:
        if count_R % 2 ==0:
            print(list(li))
        else:
            li.reverse()
            print(list(li))

### 구현 내용 설명 ###

# 1. line 10~14에서 
'''
line 10에서 입력받은 [] 제거 후,
line 11~12에서 배열에 정수가 있으면 한 숫자 씩 deque에 넣음
line 13~14에서 배열에 정수가 없으면 빈 deque 생성
'''

# 2. line 16~29에서
'''
입력 받은 p의 수 만큼 돌면서
line 18~19에서 한번에 회전하기 위해 R이 나오면 나온 수 세기
line 20에서 D가 나오면 삭제를 해야하는데,
line 21~24에서 정수가 들어있는 배열(li)이 비어있으면 error 출력
line 25에서 배열(li)이 비어있지 않으면 
line 26~27에서 R이 짝수번 나오면 회전해도 같은 배열이기 때문에 맨앞의 숫자 삭제
line 28~29에서 R이 홀수번 나오면 회전해서 역배열이 되기 때문에 맨뒤의 숫자 삭제
'''

# 3. line 33~38에서
'''
line 33에서 error이 아니라면
line 34~35에서 입력받은 p의 회전(R) 수가 짝수이면 그대로,
line 36~38에서 입력받은 p의 회전(R) 수가 홀수이면 배열의 순서를 뒤집어서 출력
'''