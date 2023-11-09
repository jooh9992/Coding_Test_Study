from collections import deque

N = int(input())

count=0
for i in range(N):
    word = deque(list(map(str, input())))
    push_li=deque()
    while word:
        if push_li:
            if push_li[-1]!=word[0]:
                push_li.append(word.popleft())
            else:
                word.popleft()
                push_li.pop()
        else:
            push_li.append(word.popleft())

    if len(push_li)==0:
        count+=1

print(count)

### 구현 내용 설명 ###

# push_li라는 deque리스트에 입력받은 단어를 한글자씩 넣기
'''
입력받은 단어 리스트(word)가 빈상태가 될 때까지 리스트의 앞 글자부터 순서대로 push_li에 넣는데,
- push_li가 비어있다면(line 10) 
  push_li의 마지막 글자와 넣어야하는 글자가 같지 않을때(line 11) push_li에 글자를 넣음(line 12)
  같다면(line 13) push_li의 마지막 글자 삭제

- push_li가 비어있지 않다면(line 16)
  넣어야 할 글자를 push_li에 넣기(line 17)
  
'''
