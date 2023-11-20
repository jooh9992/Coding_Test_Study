import sys
input = sys.stdin.readline

arr = input().rstrip()
stack = []
val = 1
count = 0

for i in range(len(arr)):
    #'('이면 +2, '['이면 +3
    if arr[i] == "(":
        stack.append(arr[i])
        val *= 2
    elif arr[i] == "[":
        stack.append(arr[i])
        val *= 3
    #')'일 때 stack이 비어있거나 마지막 문자가 '['이면 0출력
    #')'일 때 마지막 문자가 '('이면 val 값을 더해줌
    elif arr[i] == ")":
        if not stack or stack[-1] == "[":
            count = 0
            break
        if arr[i-1] == "(":
            count += val
        stack.pop()
        val //= 2
    #']'일 때 stack이 비어있거나 마지막 문자가 '('이면 0출력
    #']'일 때 마지막 문자가 '['이면 val 값을 더해줌
    else:
        if not stack or stack[-1] == "(":
            count =0
            break
        if arr[i-1] == "[":
            count += val
        stack.pop()
        val //= 3

if stack:
    print(0)
else:
    print(count)