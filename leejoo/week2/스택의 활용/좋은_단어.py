import sys
input = sys.stdin.readline

N = int(input())
count = 0

for _ in range(N):
    arr = input().strip()
    stack = []

    #stack에 값을 하나씩 넣어서 마지막 값과 같으면 pop
    #아니면 append 해줘서 최종 stack 길이가 0이면 다 짝을 지었다는
    #의미이기 때문에 count를 +1 해줌
    for i in arr:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    if len(stack) == 0:
        count += 1

print(count)