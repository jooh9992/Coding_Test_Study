from collections import deque

n=int(input())

num=1 # 스택에 넣을 수
stack=deque() 
result=[]
possi=0 # 수열을 만들 수 있을지 없을지 확인하는 변수
for i in range(n):
    input_num=int(input())
    while(num<=input_num): # 스택에 넣을 수가 입력된 수보다 작거나 같은동안 계속 진행
        stack.append(num)
        result.append('+')
        num+=1
    if stack[-1]==input_num: # 스택 마지막 값이 입력된 수와 같으면 실행
        stack.pop()
        result.append('-')
    elif stack[-1]>input_num: # 스택 마지막 값이 입력된 수보다 크면 수열을 만들 수 없음
        possi=0

if possi!=0:
    print(*result, sep='\n')
else:
    print('NO')
        
    