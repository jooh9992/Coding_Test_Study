from collections import deque

N=int(input())
queue=deque()

result=[]
for word in range(N):
    word=str(input())
    if 'push' in word:
        push, num = map(str, word.split())
        queue.append(int(num))
    if 'pop' in word:
        if len(queue)==0:
            result.append(-1)
        else:
            result.append(queue.popleft())
    if 'size' in word:
        result.append(len(queue))
    if 'empty' in word:
        if len(queue)==0:
            result.append(1)
        else:
            result.append(0)
    if 'front' in word:
        if len(queue)==0:
            result.append(-1)
        else:
            result.append(queue[0])
    if 'back' in word:
        if len(queue)==0:
            result.append(-1)
        else:
            result.append(queue[len(queue)-1])

print(result, sep='\n')