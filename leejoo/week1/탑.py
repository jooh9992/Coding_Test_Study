import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer = [0]*N #정답 배열 생성
stack = [] #스택 생성

for i in range(N):
    while stack: #스택에 값이 있을 때 
        #스택의 값이 arr[i] 값보다 작으면 필요가 없기 때문에 pop
        if arr[stack[-1][0]]<arr[i]: 
            stack.pop()
        #현재 스택에 있는 값이 다음 값보다 크면 answer에 저장
        else:
            answer[i] = stack[-1][0] + 1
            break

    #stack에 현재 위치와 값을 저장
    stack.append((i, arr[i]))

print(*answer)