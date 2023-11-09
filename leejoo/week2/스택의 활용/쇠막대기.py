import sys
input = sys.stdin.readline

arr = input().strip()
stack = []
count = 0

#배열을 입력받고 하나씩 순회하면서 진행
#"(" 이라면 stack에 넣어줌
#만약 ")"이라면 이 전 배열이 ( 이면 레이저가 맞기 때문에
#stack 마지막을 pop해주고 지금까지의 길이를 count에 저장해줌
#"))" 이런 경우라면 막대이기때문에 +1 해줌
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append('(')
    else:
        if arr[i-1] =='(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1

print(count)