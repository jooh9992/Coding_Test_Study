from collections import deque

paren = list(map(str, input()))
deq=deque()

count=0
for i in range(len(paren)):
    if paren[i]=='(':
        deq.append(paren[i])
    
    else:
        if paren[i-1]=='(':
            deq.pop()
            count+=len(deq)
        else:
            deq.pop()
            count+=1
print(count)


### 구현 내용 설명 ###

# 1. line 8~9에서 '('이 나오면 deque에 append

# 2. line 11~17에서 ')'이 나오는 경우 고려
'''
line 12~14에서 '()'인 경우 레이저로 판단하여 1번에 의해 deque에 들어간 레이저 '('를 빼고 나머지 '(' 숫자 ++
line 15~17에서 '))'인 경우 막대로 판단해 +1
'''