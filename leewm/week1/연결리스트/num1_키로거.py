from collections import deque

def keylogger(L_str, queue, queue2): 
    for word in L_str:
        if word=='<': # <이면 queue2로 알파벳 이동
            if len(queue)!=0:
                queue2.append(queue.pop())
        elif word=='>': # >이면 queue2에서 queue로 알파벳이동
            if len(queue2)!=0:
                queue.append(queue2.pop())
        elif word=='-': # -이면 queue에서 제일 위에 알파벳 제거
            if len(queue)!=0:
                queue.pop()
        else:
            queue.append(word) 

    result_queue=''.join(queue)+''.join(reversed(queue2))
    return result_queue

L=int(input()) # 테스트 케이스 수
result=[]
for i in range(L):
    L_str=map(str, input()) # 입력값 
    queue=deque()
    queue2=deque() # <할떄 pop해서 저장할 공간
    result.append(keylogger(L_str, queue, queue2))
print('\n'.join(result))

###### 테스트 케이스로 ABC<<<<<BC 

