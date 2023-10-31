import sys
input = sys.stdin.readline

n = int(input()) 
answer = [] # 정답 배열 생성
arr = [] # 수열
count = 1 # 배열을 생성하기 위한 수
a = 0 #불가능한 경우를 체크하는 변수

for i in range(n):
    num = int(input()) 

    #입력받은 수가 현재 숫자보다 크거나 같을 때
    #수열에 현재 숫자를 넣어주고 정답배열에 +를 넣어줌
    #현재 숫자를 +1해서 진행
    while count <= num: 
        arr.append(count)
        answer.append("+")
        count+=1

    #수열의 마지막 수가 num과 같을 때
    #pop을 사용하고 정답 배열에 - 을 넣어줌
    #만약 그게 아니라면 불가능한 경우이기때문에 a를 -1로 저장
    if arr[-1] == num:
        arr.pop()
        answer.append("-")
    else:
        a = -1

#만약 a가 0이면 가능한 경우여서 출력을 해주고 0이면 NO를 출력
if a == 0:
    for i in answer:
        print(i)
else:
    print("NO")
    