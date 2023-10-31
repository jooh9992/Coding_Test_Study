import sys
input = sys.stdin.readline

K = int(input()) 
arr = [] #정답 배열 생성

for _ in range(K): #K번 반복
    a = int(input()) #정수를 하나씩 입력 받음
    if a == 0 and arr: #만약 a가 0이고 정답 배열이 있으면
        arr.pop() #제일 끝 값을 삭제
    else: #0이 아니면 그 값을 arr에 저장
        arr.append(a)

print(sum(arr))