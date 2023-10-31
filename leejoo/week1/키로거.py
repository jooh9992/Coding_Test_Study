import sys
input = sys.stdin.readline

T = int(input().rstrip()) #테스트 케이스 개수 입력

for _ in range(T): #테스트 케이스 개수만큼 반복
    L = input().strip() #문자열 입력
    stack1, stack2 = [], [] #비밀번호 출력을 위한 stack 생성

    for i in L: #문자열에서 문자 하나씩 반복
        if i == "<": #왼쪽 화살표고 stack1에 값이 있다면 그 값을 stack2로 이동
            if stack1:
                stack2.append(stack1.pop())
        elif i == ">": #오른쪽 화살표고 stack2에 값이 있다면 그 값을 stack1으로 이동
            if stack2:
                stack1.append(stack2.pop())
        elif i == "-": #백스페이스를 입력하고 stack1에 값이 있다면 마지막 값을 삭제
            if stack1:
                stack1.pop()
        else: #알파벳이나 숫자이면 stack1에 값을 넣어줌
            stack1.append(i)

    #stack1과 stack2를 출력하는데 stack2는 입력을 반대로 출력해줌
    print("".join(stack1 + list(reversed(stack2))))       