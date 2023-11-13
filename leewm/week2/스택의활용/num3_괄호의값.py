from collections import deque

paren = list(input())
deq = deque()
tmp=1
sum=0

for i in range(len(paren)):
    if paren[i] == '(':
        tmp*=2
        deq.append(paren[i])
    elif paren[i] == '[':
        tmp*=3
        deq.append(paren[i])

    elif paren[i] == ')':
        if not deq or deq[-1] == '[':
            sum = 0
            break
        if paren[i-1] == '(':
            sum+=tmp
        tmp //= 2
        deq.pop()
    else:
        if not deq or deq[-1] == '(':
            sum = 0
            break
        if paren[i-1]=='[':
            sum+=tmp
        tmp//=3
        deq.pop()

if deq:
    print(0)
else:
    print(sum)

### 구현 내용 설명 ###

# line 9~14에서
'''
'('이면 +2, '['이면 +3
'''

# line 16~31에서
'''
')'일때 deq이 비어있거나 deq의 마지막 문자가 '['이면 0 리턴
')'일때 이전의 글자가 '('이면 tmp값 더하기
']'일때 deq이 비어있거나 deq의 마지막 문자가 '('이면 0 리턴
']'일때 이전의 글자가 '['이면 tmp값 더하기
'''