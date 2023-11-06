import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N, K 를 입력받음
arr = [i+1 for i in range(N)] # N 명의 배열 생성
answer = [] # 정답 배열 생성
num = 0 # 몇번째인지 계산할 변수 생성

for i in range(N): #N번만큼 반복
    num += K-1 #num에 K-1을 더해줌
    if num >= len(arr): #만약 num 수가 현재 arr 배열 길이보다 크면
        num = num % len(arr) #arr 배열 수로 나눠서 나머지를 저장

    answer.append(arr.pop(num)) #배열에서 num번째 값을 pop하고 정답배열에 저장

#출력값이 양 끝을 <>으로 변경 후 출력
print(str(answer).replace('[', '<').replace(']', '>'))